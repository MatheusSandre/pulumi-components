from typing import Optional, Mapping, Sequence

import pulumi_aws as aws
from pulumi import ResourceOptions

class CodePipeline:
    @staticmethod
    def create_pipeline(name, stores, stages, role_arn,
                        tags: Optional[Mapping[str, str]] = None,
                        depends_on: Optional[Sequence[object]] = None):
        resource_name = "pipeline-" + name

        return aws.codepipeline.Pipeline(resource_name,
                                         artifact_stores=stores,
                                         name=name,
                                         role_arn=role_arn,
                                         stages=stages,
                                         tags=tags,
                                         opts=ResourceOptions(depends_on=depends_on))
