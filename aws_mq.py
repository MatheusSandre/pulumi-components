from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import   ResourceOptions


class MQ:
    @staticmethod
    def create_broker(name,
                      engine_type: Optional[str] = None,
                      engine_version: Optional[str] = None,
                      authentication_strategy: Optional[str] = None,
                      auto_minor_version_upgrade: Optional[bool] = None,
                      host_instance_type: Optional[str] = None,
                      security_groups: Optional[Sequence[str]] = None,
                      storage_type: Optional[str] = None,
                      subnet_ids: Optional[Sequence[str]] = None,
                      publicly_accessible: Optional[bool]=None,
                      users: Optional[Sequence[str]]=None,
                      configuration: Optional[str] = None,
                      logs: Optional[str] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      depends_on: Optional[Sequence[object]] = None):
        resource_name = "mq-" + name

        return aws.mq.Broker(resource_name, apply_immediately=True,
                             authentication_strategy=authentication_strategy,
                             auto_minor_version_upgrade=auto_minor_version_upgrade,
                             broker_name=name, configuration=configuration,
                             engine_type=engine_type, engine_version=engine_version,
                             host_instance_type=host_instance_type, logs=logs,
                             publicly_accessible=publicly_accessible,
                             security_groups=security_groups, storage_type=storage_type,
                             subnet_ids=subnet_ids, users=users, tags=tags,
                             opts=ResourceOptions(depends_on=depends_on))
