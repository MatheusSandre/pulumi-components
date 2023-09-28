from typing import Optional, Mapping, Sequence

import pulumi_aws as aws
import pulumi
from pulumi import ResourceOptions

from fileloader import FileLoader

class CodeBuild:

    @staticmethod
    def create_project(name, source, service_role, environment, artifacts,
                       description: Optional[str] = None,
                       source_version: Optional[str] = None,
                       badge_enabled: Optional[bool] = None,
                       build_timeout: Optional[int] = None,
                       vpc_config: Optional[
                           pulumi.Input[pulumi.InputType['ProjectVpcConfigArgs']]] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "build-" + name

        return aws.codebuild.Project(resource_name, name=name, description=description,
                                     artifacts=artifacts, badge_enabled=badge_enabled,
                                     build_timeout=build_timeout, environment=environment,
                                     service_role=service_role, source=source,
                                     source_version=source_version, tags=tags,
                                     vpc_config=vpc_config,
                                     opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def get_buildspec_with_template(spec_configuration):
        spec = FileLoader.start_from_template(
            spec_configuration["directory"],
            spec_configuration["envs"],
            spec_configuration["file_name"],
            False,
            "YML"
        )
        return spec
