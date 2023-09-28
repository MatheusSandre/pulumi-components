from typing import Optional, Sequence
import pulumi_aws as aws
from pulumi import ResourceOptions

class KMS:

    @staticmethod
    def create_key(name,
                   policy_statements,
                   description: Optional[str] = None,
                   enabled: Optional[bool] = None,
                   depends_on: Optional[Sequence[object]] = None):
        resource_name = "kmskey-" + name

        policy = aws.iam.get_policy_document_output(statements=policy_statements)

        return aws.kms.Key(resource_name, description=description, policy=policy.json, is_enabled=enabled,
                           opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_alias(name, key_id,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "kmsalias-" + name

        return aws.kms.Alias(resource_name=resource_name, name=name, target_key_id=key_id,
                             opts=ResourceOptions(depends_on=depends_on))
