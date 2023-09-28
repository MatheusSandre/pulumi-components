from setuptools import setup
# List of requirements
requirements = []  # This could be retrieved from requirements.txt
# Package (minimal) configuration
setup(
    name="components",
    version="0.0.1",
    description="component resources",
    py_modules=["aws_alb", "alb_cloudfront", "aws_cloudwatch", "aws_codebuild", "aws_codepipeline", "aws_codestarnotification",
                "aws_dynamodb", "aws_ec2", "aws_ecr", "aws_ecs", "aws_efs", "aws_elasticache", "aws_iam", "aws_kinesis", "aws_kms",
                "aws_lambda_deployment_pipeline", "aws_lambda", "aws_mq", "aws_opensearch", "aws_rds", "aws_route53", "aws_s3",
                "aws_servicediscovery", "aws_sns", "aws_sqs", "aws_ssm", "cloudflare_dns", "cloudflare_pagerule", "fileloader"],
    # packages=find_packages(),  # __init__.py folders search
    install_requires=requirements
)
