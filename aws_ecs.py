from typing import Optional, Mapping, Sequence

import pulumi_aws as aws

from pulumi import ResourceOptions, Input, InputType

class ECS:

    @staticmethod
    def create_cluster(name,
                       container_insights_enabled: Optional[bool] = False,
                       capacity_providers: Optional[Sequence[str]] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       default_capacity_provider_strategies: Optional[
                           Sequence[Input[InputType['ClusterDefaultCapacityProviderStrategyArgs']]]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "ecscluster-" + name

        if container_insights_enabled:
            settings = ECS.settings_list_with_container_insights()
        else:
            settings = None

        return aws.ecs.Cluster(resource_name, name=name, settings=settings, capacity_providers=capacity_providers,
                               tags=tags, default_capacity_provider_strategies=default_capacity_provider_strategies,
                               opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_service(name,
                       cluster_arn: Optional[str] = None,
                       task_definition: Optional[str] = None,
                       enable_ecs_managed_tags: Optional[bool] = None,
                       propagate_tags: Optional[str] = None,
                       load_balancers: Optional[Sequence[Input[InputType['ServiceLoadBalancerArgs']]]] = None,
                       network_configuration: Optional[Input[InputType['ServiceNetworkConfigurationArgs']]] = None,
                       capacity_provider_strategies: Optional[Sequence[
                           Input[InputType['ServiceCapacityProviderStrategyArgs']]]] = None,
                       deployment_minimum_healthy_percent: Optional[int] = None,
                       deployment_maximum_percent: Optional[int] = None,
                       service_registries: Optional[Input[InputType['ServiceServiceRegistriesArgs']]] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       enable_execute_command: Optional[bool] = None,
                       deployment_circuit_breaker: Optional[Input[InputType['ServiceDeploymentCircuitBreakerArgs']]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "ecsservice-" + name

        return aws.ecs.Service(resource_name, name=name, cluster=cluster_arn, task_definition=task_definition,
                               enable_ecs_managed_tags=enable_ecs_managed_tags, propagate_tags=propagate_tags,
                               load_balancers=load_balancers, network_configuration=network_configuration,
                               deployment_maximum_percent=deployment_maximum_percent,
                               deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
                               capacity_provider_strategies=capacity_provider_strategies,
                               service_registries=service_registries, tags=tags,
                               enable_execute_command=enable_execute_command,
                               deployment_circuit_breaker=deployment_circuit_breaker,
                               opts=ResourceOptions(
                                   ignore_changes=[
                                       "task_definition", "desired_count", "capacity_provider_strategies"],
                                   depends_on=depends_on))

    @staticmethod
    def create_task_definition(name,
                               network_mode: Optional[str] = None,
                               cpu: Optional[str] = None,
                               memory: Optional[str] = None,
                               requires_compatibilities: Optional[Sequence[str]] = None,
                               tags: Optional[Mapping[str, str]] = None,
                               task_role_arn: Optional[str] = None,
                               execution_role_arn: Optional[str] = None,
                               container_definitions: Optional[str] = None,
                               volumes: Optional[Sequence[Input[InputType['TaskDefinitionVolumeArgs']]]] = None,
                               ignore_container_definitions_changes: Optional[bool] = True,
                               depends_on: Optional[Sequence[object]] = None):
        resource_name = "ecstaskdefinition-" + name

        if ignore_container_definitions_changes:
            ignore_changes = ["container_definitions"]
            container_definitions = "[{}]"
        else:
            ignore_changes = []

        task = aws.ecs.TaskDefinition(resource_name, family=name, network_mode=network_mode,
                                      container_definitions=container_definitions, cpu=cpu, memory=memory,
                                      requires_compatibilities=requires_compatibilities,
                                      tags=tags, task_role_arn=task_role_arn,
                                      execution_role_arn=execution_role_arn, volumes=volumes,
                                      opts=ResourceOptions(ignore_changes=ignore_changes, protect=False,
                                                           depends_on=depends_on))

        return task

    @ staticmethod
    def settings_list_with_container_insights():
        settings= [
            {
                "name": "containerInsights",
                "value": "enabled"
            }
        ]

        return settings
