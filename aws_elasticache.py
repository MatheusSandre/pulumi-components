from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions


class Elasticache:
    @staticmethod
    def create_cluster(name,
                       engine: Optional[str] = None,
                       engine_version: Optional[str] = None,
                       node_type: Optional[str] = None,
                       num_cache_nodes: Optional[int] = None,
                       port: Optional[int] = None,
                       parameter_group_name: Optional[str] = None,
                       az_mode: Optional[str] = None,
                       subnet_group_name: Optional[str] = None,
                       security_group_ids: Optional[Sequence[str]] = None,
                       snapshot_name: Optional[str] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "elasticachecluster-" + name

        return aws.elasticache.Cluster(resource_name, az_mode=az_mode, cluster_id=name, engine=engine,
                                       engine_version=engine_version, node_type=node_type,
                                       num_cache_nodes=num_cache_nodes, apply_immediately=True,
                                       parameter_group_name=parameter_group_name, snapshot_name=snapshot_name,
                                       port=port, security_group_ids=security_group_ids,
                                       subnet_group_name=subnet_group_name, tags=tags,
                                       opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    # pylint: disable=too-many-arguments
    def create_replication(name,
                           description="managed by pulumi",
                           engine: Optional[str] = None,
                           engine_version: Optional[str] = None,
                           cluster_mode: Optional[Input[InputType['ReplicationGroupClusterModeArgs']]] = None,
                           automatic_failover_enabled: Optional[bool] = None,
                           node_type: Optional[str] = None,
                           number_cache_clusters: Optional[int] = None,
                           port: Optional[int] = None,
                           parameter_group_name: Optional[str] = None,
                           multi_az_enabled: Optional[bool] = None,
                           subnet_group_name: Optional[str] = None,
                           num_node_groups: Optional[int] = None,
                           replicas_per_node_group: Optional[int] = None,
                           security_group_ids: Optional[Sequence[str]] = None,
                           snapshot_retention_limit: Optional[int] = None,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "elasticachereplication-" + name

        replication = aws.elasticache.ReplicationGroup(resource_name, automatic_failover_enabled=automatic_failover_enabled,
                                                       cluster_mode=cluster_mode, engine=engine,
                                                       engine_version=engine_version, num_node_groups=num_node_groups,
                                                       number_cache_clusters=number_cache_clusters,
                                                       node_type=node_type, parameter_group_name=parameter_group_name,
                                                       port=port, description=description, replicas_per_node_group=replicas_per_node_group,
                                                       replication_group_id=name, security_group_ids=security_group_ids,
                                                       subnet_group_name=subnet_group_name, multi_az_enabled=multi_az_enabled,
                                                       snapshot_retention_limit=snapshot_retention_limit, tags=tags,
                                                       opts=ResourceOptions(depends_on=depends_on))

        return replication

    @staticmethod
    def create_subnet_group(name, subnet_ids,
                            description: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "elasticachesubnetgroup-" + name

        return aws.elasticache.SubnetGroup(resource_name, description=description, name=name, subnet_ids=subnet_ids,
                                           opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_parameter_group(name, family,
                               description: Optional[str] = None,
                               parameters: Optional[Sequence[Input[InputType['ParameterGroupParameterArgs']]]] = None,
                               depends_on: Optional[Sequence[object]] = None):
        resource_name = "elasticacheparametergroup-" + name

        return aws.elasticache.ParameterGroup(resource_name, description=description, family=family, name=name,
                                              parameters=parameters, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def get_cluster(name):
        return aws.elasticache.get_cluster(cluster_id=name)
