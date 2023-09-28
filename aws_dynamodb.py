from typing import Optional, Sequence, Mapping

import pulumi
import pulumi_aws as aws

from pulumi import ResourceOptions

class DynamoDB:
    @staticmethod
    def create_table(name, attributes, hash_key,
                     billing_mode: Optional[str] = None,
                     range_key: Optional[str] = None,
                     read_capacity: Optional[int] = None,
                     write_capacity: Optional[int] = None,
                     ttl: Optional[pulumi.Input[pulumi.InputType['TableTtlArgs']]] = None,
                     stream_enabled: Optional[int] = False,
                     stream_view_type: Optional[str] = None,
                     secondary_indexes: Optional[Sequence[
                         pulumi.Input[pulumi.InputType['TableLocalSecondaryIndexArgs']]]] = None,
                     global_secondary_indexes: Optional[Sequence[
                         pulumi.Input[pulumi.InputType[aws.dynamodb.TableGlobalSecondaryIndexArgs]]]] = None,
                     server_side_encryption: Optional[aws.dynamodb.TableServerSideEncryptionArgs] = None,
                     tags: Optional[Mapping[str, str]] = None,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "dynamodbtable-" + name

        if "prod" in pulumi.get_stack():
            point_in_time_recovery = {
                "enabled": True
            }
        else:
            point_in_time_recovery = None

        return aws.dynamodb.Table(resource_name, name=name, attributes=attributes,
                                  billing_mode=billing_mode, hash_key=hash_key,
                                  range_key=range_key, read_capacity=read_capacity,
                                  write_capacity=write_capacity, ttl=ttl, tags=tags,
                                  local_secondary_indexes=secondary_indexes,
                                  global_secondary_indexes=global_secondary_indexes,
                                  stream_enabled=stream_enabled,
                                  stream_view_type=stream_view_type,
                                  point_in_time_recovery=point_in_time_recovery,
                                  server_side_encryption=server_side_encryption,
                                  opts=ResourceOptions(
                                      ignore_changes=["write_capacity", "read_capacity"],
                                      depends_on=depends_on
                                  ))
