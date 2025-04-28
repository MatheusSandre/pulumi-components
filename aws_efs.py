from typing import Optional, Mapping, Sequence

import pulumi_aws as aws
from pulumi import Input, InputType, ResourceOptions


class EFS:
    @staticmethod
    def create_filesystem(name,
                          availability_zone_name: Optional[str] = None,
                          creation_token: Optional[str] = None,
                          encrypted: Optional[bool] = None,
                          kms_key_id: Optional[str] = None,
                          lifecycle_policies: Optional[Input[InputType['FileSystemLifecyclePolicyArgs']]] = None,
                          performance_mode: Optional[str] = None,
                          provisioned_throughput_in_mibps: Optional[float] = None,
                          throughput_mode: Optional[str] = None,
                          tags: Optional[Mapping[str, str]] = None,
                          depends_on: Optional[Sequence[object]] = None):
        resource_name = "efsfilesystem-" + name

        return aws.efs.FileSystem(resource_name,
                                  availability_zone_name=availability_zone_name,
                                  creation_token=creation_token, encrypted=encrypted,
                                  kms_key_id=kms_key_id, lifecycle_policies=lifecycle_policies,
                                  performance_mode=performance_mode,
                                  provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
                                  tags=tags, throughput_mode=throughput_mode,
                                  opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_mounttarget(name,
                           file_system_id: Optional[str] = None,
                           ip_address: Optional[str] = None,
                           security_groups: Optional[Sequence[str]] = None,
                           subnet_id: Optional[str] = None,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "efsmounttarget-" + name

        return aws.efs.MountTarget(resource_name,
                                   file_system_id=file_system_id,
                                   ip_address=ip_address,
                                   security_groups=security_groups,
                                   subnet_id=subnet_id,
                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_accesspoint(name,
                           file_system_id: Optional[str] = None,
                           posix_user: Optional[Sequence[object]] = None,
                           root_directory: Optional[Sequence[object]] = None,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "efsaccesspoint-" + name

        return aws.efs.AccessPoint(resource_name,
                                   file_system_id=file_system_id,
                                   posix_user=posix_user,
                                   root_directory=root_directory,
                                   tags=tags,
                                   opts=ResourceOptions(depends_on=depends_on))
