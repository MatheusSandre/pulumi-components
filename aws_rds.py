from typing import Optional, Mapping, Sequence, Union
import pulumi_aws as aws

from pulumi import ResourceOptions, Input, InputType


class RDS:
    @staticmethod
    # pylint: disable=too-many-arguments
    def create_cluster(name,
                       engine_mode: Optional[Union[str,
                                                   Input[InputType['EngineMode']]]] = None,
                       engine: Optional[Union[str,
                                              Input[InputType['EngineMode']]]] = None,
                       engine_version: Optional[str] = None,
                       db_cluster_parameter_group_name: Optional[str] = None,
                       database_name: Optional[str] = None,
                       username: Optional[str] = None,
                       password: Optional[str] = None,
                       port: Optional[int] = None,
                       db_subnet_group_name: Optional[str] = None,
                       vpc_security_group_ids: Optional[Sequence[str]] = None,
                       cluster_members: Optional[Sequence[str]] = None,
                       backup_retention_period: Optional[int] = None,
                       copy_tags_to_snapshot: Optional[bool] = False,
                       deletion_protection: Optional[bool] = False,
                       enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None,
                       skip_final_snapshot: Optional[bool] = False,
                       tags: Optional[Mapping[str, str]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "rdscluster" + name

        return aws.rds.Cluster(resource_name, backup_retention_period=backup_retention_period,
                               cluster_identifier=name, cluster_members=cluster_members,
                               copy_tags_to_snapshot=copy_tags_to_snapshot,
                               database_name=database_name,
                               db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                               db_subnet_group_name=db_subnet_group_name, deletion_protection=deletion_protection,
                               enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                               engine=engine, engine_mode=engine_mode, engine_version=engine_version,
                               master_password=password, master_username=username, port=port,
                               skip_final_snapshot=skip_final_snapshot, tags=tags,
                               vpc_security_group_ids=vpc_security_group_ids,
                               opts=ResourceOptions(ignore_changes=["master_username", "master_password"],
                                                    depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_instance(db_name, instance_class,
                        iam_database_authentication_enabled: Optional[bool] = None,
                        apply_immediately: Optional[bool] = None,
                        username: Optional[str] = None,
                        password: Optional[str] = None,
                        port: Optional[int] = None,
                        allocated_storage: Optional[int] = None,
                        db_subnet_group_name: Optional[str] = None,
                        vpc_security_group_ids: Optional[Sequence[str]] = None,
                        engine: Optional[str] = None,
                        engine_version: Optional[str] = None,
                        storage_encrypted: Optional[bool] = False,
                        storage_type: Optional[Union[str,
                                                     Input[InputType['StorageType']]]] = None,
                        monitoring_interval: Optional[int] = None,
                        monitoring_role_arn: Optional[str] = None,
                        option_group_name: Optional[str] = None,
                        parameter_group_name: Optional[str] = None,
                        publicly_accessible: Optional[bool] = False,
                        performance_insights_enabled: Optional[bool] = False,
                        skip_final_snapshot: Optional[bool] = False,
                        auto_minor_version_upgrade: Optional[bool] = False,
                        multi_az: Optional[bool] = False,
                        backup_retention_period: Optional[int] = None,
                        enabled_cloudwatch_logs_exports: Optional[Sequence[str]] = None,
                        tags: Optional[Mapping[str, str]] = None,
                        depends_on: Optional[Sequence[object]] = None):
        resource_name = "rdsinstance-" + db_name

        return aws.rds.Instance(resource_name, auto_minor_version_upgrade=auto_minor_version_upgrade,
                                backup_retention_period=backup_retention_period,
                                db_subnet_group_name=db_subnet_group_name, identifier=db_name,
                                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                                engine=engine, engine_version=engine_version, apply_immediately=apply_immediately,
                                instance_class=instance_class, monitoring_interval=monitoring_interval,
                                multi_az=multi_az, db_name=db_name, option_group_name=option_group_name,
                                parameter_group_name=parameter_group_name, password=password,
                                performance_insights_enabled=performance_insights_enabled, port=port,
                                publicly_accessible=publicly_accessible, skip_final_snapshot=skip_final_snapshot,
                                storage_encrypted=storage_encrypted, storage_type=storage_type, tags=tags,
                                username=username, vpc_security_group_ids=vpc_security_group_ids,
                                allocated_storage=allocated_storage, monitoring_role_arn=monitoring_role_arn,
                                iam_database_authentication_enabled=iam_database_authentication_enabled,
                                opts=ResourceOptions(ignore_changes=["username", "password"],
                                                     depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_cluster_instance(name, cluster_identifier, instance_class,
                                identifier: Optional[str] = None,
                                db_subnet_group_name: Optional[str] = None,
                                engine: Optional[str] = None,
                                engine_version: Optional[str] = None,
                                monitoring_interval: Optional[int] = None,
                                monitoring_role_arn: Optional[str] = None,
                                copy_tags_to_snapshot: Optional[bool] = False,
                                db_parameter_group_name: Optional[str] = None,
                                publicly_accessible: Optional[bool] = False,
                                performance_insights_enabled: Optional[bool] = False,
                                auto_minor_version_upgrade: Optional[bool] = False,
                                apply_immediately: Optional[bool] = False,
                                tags: Optional[Mapping[str, str]] = None,
                                depends_on: Optional[Sequence[object]] = None):
        resource_name = "rdsclusterinstance-" + name

        return aws.rds.ClusterInstance(resource_name, apply_immediately=apply_immediately,
                                       auto_minor_version_upgrade=auto_minor_version_upgrade,
                                       cluster_identifier=cluster_identifier,
                                       copy_tags_to_snapshot=copy_tags_to_snapshot,
                                       db_parameter_group_name=db_parameter_group_name,
                                       db_subnet_group_name=db_subnet_group_name,
                                       engine=engine, engine_version=engine_version,
                                       identifier=identifier, instance_class=instance_class,
                                       monitoring_interval=monitoring_interval,
                                       monitoring_role_arn=monitoring_role_arn,
                                       performance_insights_enabled=performance_insights_enabled,
                                       publicly_accessible=publicly_accessible, tags=tags,
                                       opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_subnet_group(name, subnet_ids,
                            tags: Optional[Mapping[str, str]] = None,
                            depends_on: Optional[Sequence[object]] = None):

        resource_name = "rdssubnetgroup-" + name

        return aws.rds.SubnetGroup(resource_name, name=name, subnet_ids=subnet_ids,
                                   tags=tags, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_parameter_group(name, family,
                               parameters,
                               tags: Optional[Mapping[str, str]] = None,
                               depends_on: Optional[Sequence[object]] = None):

        resource_name = "rdsparametergroup-" + name

        return aws.rds.ParameterGroup(resource_name, family=family, name=name,
                                      parameters=parameters, tags=tags,
                                      opts=ResourceOptions(depends_on=depends_on))
