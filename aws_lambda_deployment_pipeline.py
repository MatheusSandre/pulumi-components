from aws_codebuild import CodeBuild
from aws_codepipeline import CodePipeline
from aws_codestarnotification import CodeStarNotification

class LambdaDeploymentPipeline:
    @staticmethod
    def create_resources(branch_name, git_repo, lambda_name_in_aws, path_begin, main_path, version, tags, aws_region,
                         policies_roles, codestar_arn, sns_notification_arn, s3_codepipeline):
        if version:
            name = f"{lambda_name_in_aws}-{version}"
            buildspec_file = "build-lambda-with-version"
        else:
            name = lambda_name_in_aws
            buildspec_file = "build-lambda"

        spec = CodeBuild.get_buildspec_with_template(
            {
                "file_name": buildspec_file,
                "directory": "./resources/aws/codebuild",
                "envs": {
                    "path_begin": path_begin,
                    "lambda_name_in_aws": lambda_name_in_aws,
                    "main_path": main_path,
                    "version": version,
                    "aws_region": aws_region
                }
            }
        )

        lambda_build = CodeBuild.create_project(
            name=f"lambda-{name}",
            source={
                "type": "CODEPIPELINE",
                "buildspec": spec
            },
            build_timeout=60,
            artifacts={
                "type": "CODEPIPELINE"
            },
            environment={
                "compute_type": "BUILD_GENERAL1_SMALL",
                "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0",
                "type": "LINUX_CONTAINER",
                "privileged_mode": False
            },
            service_role=policies_roles["codebuild_lambda_role"],
            tags=tags
        )

        stages = [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "Source",
                        "category": "Source",
                        "owner": "AWS",
                        "provider": "CodeStarSourceConnection",
                        "version": "1",
                        "outputArtifacts": [name],
                        "configuration": {
                            "ConnectionArn": codestar_arn,
                            "BranchName": f"{branch_name}",
                            "DetectChanges": "false",
                            "FullRepositoryId": git_repo
                        },
                        "inputArtifacts": None,
                        "region": aws_region
                    }
                ]
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "Build",
                        "category": "Build",
                        "owner": "AWS",
                        "provider": "CodeBuild",
                        "version": "1",
                        "configuration": {
                            "ProjectName": lambda_build.name
                        },
                        "inputArtifacts": [name],
                        "outputArtifacts": None,
                        "region": aws_region
                    }
                ]
            }
        ]

        codepipeline_lambda = CodePipeline.create_pipeline(
            name=f"lambda-{name}",
            stores=[{
                "type": "S3",
                "location": s3_codepipeline
            }],
            stages=stages,
            role_arn=policies_roles["codepipeline_lambda_role"],
            tags=tags,
        )

        CodeStarNotification.create_notification_rule(
            name=f"notification-{name}",
            detail_type="FULL",
            event_type_ids=[
                "codepipeline-pipeline-stage-execution-succeeded",
                "codepipeline-pipeline-stage-execution-failed",
                "codepipeline-pipeline-stage-execution-started",
                "codepipeline-pipeline-stage-execution-canceled",
                "codepipeline-pipeline-stage-execution-resumed"
            ],
            resource=codepipeline_lambda.arn,
            status="ENABLED",
            tags=tags,
            targets=[
                {
                    "address": sns_notification_arn,
                    "type": "SNS"
                }
            ]
        )
