from typing import Optional, Mapping, Sequence, Union
import pulumi_aws as aws

import pulumi

from pulumi import ResourceOptions, Input, InputType

class Lambda:
    @staticmethod
    def create_function(name, role,
                        description: Optional[str] = None,
                        handler: Optional[str] = None,
                        runtime: Optional[Union[str, Input[InputType['Runtime']]]] = None,
                        timeout: Optional[int] = None,
                        memory_size: Optional[int] = None,
                        tags: Optional[Mapping[str, str]] = None,
                        environment: Optional[Input[InputType['FunctionEnvironmentArgs']]] = None,
                        vpc_config: Optional[Input[InputType['FunctionVpcConfigArgs']]] = None,
                        layers: Optional[Sequence[str]] = None,
                        reserved_concurrent_executions: Optional[int] = None,
                        package_type: Optional[pulumi.Input[str]] = None,
                        image_uri: Optional[pulumi.Input[str]] = None,
                        depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdafunction-" + name

        if not runtime:
            sample_code = None
        elif runtime.startswith("go"):
            sample_code = pulumi.AssetArchive(
                {"main": pulumi.FileArchive("./lambda_examples")}
            )
        elif runtime.startswith("python"):
            sample_code = pulumi.AssetArchive(
                {"main.py": pulumi.FileArchive("./lambda_examples")}
            )
        elif runtime.startswith("nodejs"):
            sample_code = pulumi.AssetArchive(
                {"index.js": pulumi.FileArchive("./lambda_examples")}
            )
        elif runtime.startswith("ruby"):
            sample_code = pulumi.AssetArchive(
                {"lambda_function.rb": pulumi.FileArchive("./lambda_examples")}
            )

        return aws.lambda_.Function(resource_name, description=description, handler=handler,
                                    runtime=runtime, role=role, tags=tags, name=name,
                                    timeout=timeout, memory_size=memory_size, environment=environment,
                                    vpc_config=vpc_config, code=sample_code, layers=layers,
                                    reserved_concurrent_executions=reserved_concurrent_executions,
                                    package_type=package_type, image_uri=image_uri,
                                    opts=ResourceOptions(ignore_changes=["code"], depends_on=depends_on))

    @staticmethod
    def create_layer_version(name,
                             compatible_runtimes: Optional[Sequence[str]] = None,
                             description: Optional[str] = None,
                             depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdalayer-" + name

        for runtime in compatible_runtimes:
            if runtime.startswith("python"):
                sample_code = pulumi.AssetArchive(
                    {"sample_python.zip": pulumi.FileArchive("./components/lambda_examples/layers")}
                )
            elif runtime.startswith("go"):
                sample_code = pulumi.AssetArchive(
                    {"sample_go.zip": pulumi.FileArchive("./components/lambda_examples/layers")}
                )
            elif runtime.startswith("nodejs"):
                sample_code = pulumi.AssetArchive(
                    {"sample_nodejs.zip": pulumi.FileArchive("./components/lambda_examples/layers")}
                )
            elif runtime.startswith("ruby"):
                sample_code = pulumi.AssetArchive(
                    {"sample_ruby.zip": pulumi.FileArchive("./components/lambda_examples/layers")}
                )

        return aws.lambda_.LayerVersion(resource_name, compatible_runtimes=compatible_runtimes, code=sample_code,
                                        description=description, layer_name=name,
                                        opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def event_source_mapping(name, event_source_arn, function_arn,
                             batch_size: Optional[int] = None,
                             maximum_batching_window_in_seconds: Optional[int] = None,
                             starting_position: Optional[str] = None,
                             depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdaeventsourcemapping-" + name

        return aws.lambda_.EventSourceMapping(resource_name, event_source_arn=event_source_arn, batch_size=batch_size,
                                              maximum_batching_window_in_seconds=maximum_batching_window_in_seconds,
                                              function_name=function_arn, starting_position=starting_position,
                                              opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_resource_base_policy(name, action, principal, function,
                                    statement_id: Optional[str] = None,
                                    qualifier: Optional[str] = None,
                                    source_arn: Optional[str] = None,
                                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdaresourcebasepolicy-" + name

        return aws.lambda_.Permission(resource_name, action=action, function=function, qualifier=qualifier,
                                      principal=principal, source_arn=source_arn,
                                      statement_id=statement_id,
                                      opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_alias(name, function_name, function_version,
                     description: Optional[str] = None,
                     routing_config: Optional[Input[InputType['AliasRoutingConfigArgs']]] = None,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdaalias-" + function_name + "-" + name

        return aws.lambda_.Alias(resource_name, description=description,
                                 function_name=function_name, name=name,
                                 function_version=function_version,
                                 routing_config=routing_config,
                                 opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_concurrency_config(function_name,
                                  concurrent_executions,
                                  qualifier: Optional[str] = None,
                                  depends_on: Optional[Sequence[object]] = None):
        resource_name = "lambdaconcurrency-" + function_name

        return aws.lambda_.ProvisionedConcurrencyConfig(resource_name,
                                                        function_name=function_name,
                                                        provisioned_concurrent_executions=concurrent_executions,
                                                        qualifier=qualifier,
                                                        opts=ResourceOptions(depends_on=depends_on))
