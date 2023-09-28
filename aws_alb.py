from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions

class LoadBalancer:
    @staticmethod
    def create_load_balancer(name,
                             load_balancer_type: Optional[str] = None,
                             is_internal: Optional[bool] = False,
                             ip_address_type: Optional[str] = None,
                             security_groups: Optional[Sequence[str]] = None,
                             idle_timeout: Optional[int] = None,
                             subnets: Optional[Sequence[str]] = None,
                             tags: Optional[Mapping[str, str]] = None,
                             depends_on: Optional[Sequence[object]] = None):
        resource_name = "loadbalancer-" + name

        return aws.lb.LoadBalancer(resource_name, internal=is_internal, ip_address_type=ip_address_type,
                                   load_balancer_type=load_balancer_type, name=name,
                                   drop_invalid_header_fields=True,
                                   security_groups=security_groups,
                                   idle_timeout=idle_timeout, subnets=subnets,
                                   tags=tags,
                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_target_group(name,
                            health_check: Optional[
                                Input[InputType['TargetGroupHealthCheckArgs']]] = None,
                            deregistration_delay: Optional[int] = None,
                            target_type: Optional[str] = None,
                            lambda_multi_value_headers_enabled: Optional[bool] = False,
                            port: Optional[int] = None,
                            protocol: Optional[str] = None,
                            vpc_id: Optional[str] = None,
                            tags: Optional[Mapping[str, str]] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "targetgroup-" + name

        return aws.lb.TargetGroup(resource_name, deregistration_delay=deregistration_delay,
                                  health_check=health_check, vpc_id=vpc_id,
                                  lambda_multi_value_headers_enabled=lambda_multi_value_headers_enabled,
                                  name=name, port=port, protocol=protocol,
                                  tags=tags, target_type=target_type,
                                  opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def target_group_attachment(name, target_group_arn, target_id,
                                port: Optional[int] = None,
                                availability_zone: Optional[str] = None,
                                depends_on: Optional[Sequence[object]] = None):
        resource_name = "targetgroupattach-" + name

        return aws.lb.TargetGroupAttachment(resource_name, availability_zone=availability_zone,
                                            port=port, target_group_arn=target_group_arn,
                                            target_id=target_id,
                                            opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_listener(name, default_actions, load_balancer_arn,
                        certificate_arn: Optional[str] = None,
                        ssl_policy: Optional[str] = None,
                        port: Optional[int] = None,
                        protocol: Optional[str] = None,
                        depends_on: Optional[Sequence[object]] = None):
        resource_name = "lblistener-" + name

        return aws.lb.Listener(resource_name,
                               certificate_arn=certificate_arn, default_actions=default_actions,
                               load_balancer_arn=load_balancer_arn, port=port, protocol=protocol,
                               ssl_policy=ssl_policy,
                               opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_listener_rule(name, conditions, actions,
                             listener_arn: Optional[str] = None,
                             priority: Optional[int] = None,
                             depends_on: Optional[Sequence[object]] = None):
        resource_name = "lblistenerrule-" + name

        return aws.lb.ListenerRule(resource_name, actions=actions, conditions=conditions,
                                   listener_arn=listener_arn, priority=priority,
                                   opts=ResourceOptions(depends_on=depends_on))
