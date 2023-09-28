from typing import Optional, Mapping, Sequence

import pulumi_aws as aws
from pulumi import Input, InputType, ResourceOptions

class ECR:
    @staticmethod
    def create_repository(name,
                          image_tag_mutability: Optional[str] = None,
                          image_scanning_configuration: Optional[
                              Input[InputType['RepositoryImageScanningConfigurationArgs']]] = None,
                          tags: Optional[Mapping[str, str]] = None,
                          depends_on: Optional[Sequence[object]] = None):
        resource_name = "ecrrepository-" + name

        return aws.ecr.Repository(resource_name,
                                  image_scanning_configuration=image_scanning_configuration,
                                  image_tag_mutability=image_tag_mutability,
                                  name=name, tags=tags,
                                  opts=ResourceOptions(depends_on=depends_on))
