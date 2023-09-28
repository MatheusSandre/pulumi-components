from typing import Optional, Sequence
import pulumi_aws as aws

from pulumi import ResourceOptions

class SSM:
    @staticmethod
    def create_parameter(name, parameter_type,
                         value=" ",
                         key_id: Optional[str] = None,
                         depends_on: Optional[Sequence[object]] = None):
        resource_name = "ssmparameter" + name

        return aws.ssm.Parameter(resource_name, name=name, value=value, type=parameter_type, key_id=key_id,
                                 opts=ResourceOptions(ignore_changes=[], depends_on=depends_on))

    @staticmethod
    def get_parameter(name,
                      with_decryption: Optional[bool] = None,):
        return aws.ssm.get_parameter(name, with_decryption)
