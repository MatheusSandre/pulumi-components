from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions


class DocumentDB:
    @staticmethod
    # pylint: disable=too-many-arguments
    def create_cluster(name,
                       master_username: Optional[str] = None,
                       master_password: Optional[str] = None,
                       engine: str = "docdb",
                       engine_version: Optional[str] = None,
                       port: int = 27017,
                       db_subnet_group_name: Optional[str] = None,
                       vpc_security_group_ids: Optional[Sequence[str]] = None,
                       db_cluster_parameter_group_name: Optional[str] = None,
                       backup_retention_period: Optional[int] = 7,
                       preferred_backup_window: Optional[str] = "03:00-04:00",
                       preferred_maintenance_window: Optional[str] = "sun:04:00-sun:05:00",
                       deletion_protection: Optional[bool] = True,
                       skip_final_snapshot: Optional[bool] = False,
                       storage_encrypted: Optional[bool] = True,
                       enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None,
                       apply_immediately: Optional[bool] = True,
                       tags: Optional[Mapping[str, str]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "docdbcluster-" + name

        return aws.docdb.Cluster(resource_name,
                                 cluster_identifier=name,
                                 engine=engine,
                                 engine_version=engine_version,
                                 master_username=master_username,
                                 master_password=master_password,
                                 port=port,
                                 db_subnet_group_name=db_subnet_group_name,
                                 vpc_security_group_ids=vpc_security_group_ids,
                                 db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                                 backup_retention_period=backup_retention_period,
                                 preferred_backup_window=preferred_backup_window,
                                 preferred_maintenance_window=preferred_maintenance_window,
                                 deletion_protection=deletion_protection,
                                 skip_final_snapshot=skip_final_snapshot,
                                 storage_encrypted=storage_encrypted,
                                 enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                                 apply_immediately=apply_immediately,
                                 tags=tags,
                                 opts=ResourceOptions(
                                     ignore_changes=["master_username", "master_password"],
                                     depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_cluster_instance(name, cluster_identifier, instance_class,
                                identifier: Optional[str] = None,
                                engine: str = "docdb",
                                auto_minor_version_upgrade: Optional[bool] = True,
                                apply_immediately: Optional[bool] = True,
                                preferred_maintenance_window: Optional[str] = "sun:04:00-sun:05:00",
                                tags: Optional[Mapping[str, str]] = None,
                                depends_on: Optional[Sequence[object]] = None):
        resource_name = "docdbclusterinstance-" + name

        return aws.docdb.ClusterInstance(resource_name,
                                         identifier=identifier or name,
                                         cluster_identifier=cluster_identifier,
                                         instance_class=instance_class,
                                         engine=engine,
                                         apply_immediately=apply_immediately,
                                         auto_minor_version_upgrade=auto_minor_version_upgrade,
                                         preferred_maintenance_window=preferred_maintenance_window,
                                         tags=tags,
                                         opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_subnet_group(name, subnet_ids,
                            description: Optional[str] = None,
                            tags: Optional[Mapping[str, str]] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "docdbsubnetgroup-" + name

        return aws.docdb.SubnetGroup(resource_name,
                                     name=name,
                                     subnet_ids=subnet_ids,
                                     description=description,
                                     tags=tags,
                                     opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_cluster_parameter_group(name, family,
                                       description: Optional[str] = None,
                                       parameters: Optional[Sequence[Input[InputType['ClusterParameterGroupParameterArgs']]]] = None,
                                       tags: Optional[Mapping[str, str]] = None,
                                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "docdbclusterparametergroup-" + name

        return aws.docdb.ClusterParameterGroup(resource_name,
                                               name=name,
                                               family=family,
                                               description=description,
                                               parameters=parameters,
                                               tags=tags,
                                               opts=ResourceOptions(depends_on=depends_on))
