from typing import Optional, Union, Sequence, Mapping
import pulumi_aws as aws

import pulumi
from pulumi import Input, InputType, ResourceOptions

class EC2:
    @staticmethod
    def create_instance(name, ami,
                        associate_public_ip_address: Optional[bool] = False,
                        ebs_optimized: Optional[bool] = False,
                        iam_instance_profile: Optional[str] = None,
                        instance_type: Optional[
                            Union[str, pulumi.Input[pulumi.InputType['InstanceType']]]] = None,
                        disable_api_termination: Optional[bool] = None,
                        root_block_device: Optional[
                            pulumi.Input[pulumi.InputType['InstanceRootBlockDeviceArgs']]] = None,
                        security_groups: Optional[Sequence[str]] = None,
                        subnet_id: Optional[str] = None,
                        key_name: Optional[str] = None,
                        tags: Optional[Mapping[str, str]] = None,
                        depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2instance-" + name

        return aws.ec2.Instance(resource_name, ami=ami, associate_public_ip_address=associate_public_ip_address,
                                ebs_optimized=ebs_optimized, iam_instance_profile=iam_instance_profile,
                                instance_type=instance_type, disable_api_termination=disable_api_termination,
                                root_block_device=root_block_device, key_name=key_name, vpc_security_group_ids=security_groups,
                                subnet_id=subnet_id, tags=tags, volume_tags=tags,
                                opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_vpc(name, cidr_block,
                   enable_dns_hostnames: Optional[bool] = None,
                   enable_dns_support: Optional[bool] = None,
                   tags: Optional[Mapping[str, str]] = None,
                   depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2vpc-" + name

        return aws.ec2.Vpc(resource_name,
                           cidr_block=cidr_block,
                           enable_dns_hostnames=enable_dns_hostnames,
                           enable_dns_support=enable_dns_support,
                           tags=tags,
                           opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_subnet(name, vpc_id, cidr_block,
                      map_public_ip_on_launch: Optional[bool] = None,
                      availability_zone: Optional[str] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2subnet-" + name

        return aws.ec2.Subnet(resource_name, vpc_id=vpc_id, cidr_block=cidr_block, availability_zone=availability_zone,
                              map_public_ip_on_launch=map_public_ip_on_launch, tags=tags,
                              opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_internet_gateway(name,
                                vpc_id: Optional[bool] = None,
                                tags: Optional[Mapping[str, str]] = None,
                                depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2igw-" + name

        return aws.ec2.InternetGateway(resource_name,
                                       vpc_id=vpc_id,
                                       tags=tags,
                                       opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_route_table(name, vpc_id,
                           routes: Optional[
                               Sequence[pulumi.Input[pulumi.InputType['RouteTableRouteArgs']]]] = None,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2routetable-" + name

        return aws.ec2.RouteTable(resource_name, vpc_id=vpc_id, routes=routes, tags=tags,
                                  opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_route_table_association(name, route_table_id,
                                       subnet_id: Optional[str] = None,
                                       depends_on: Optional[Sequence[object]] = None):
        resource_name = name

        return aws.ec2.RouteTableAssociation(resource_name, subnet_id=subnet_id, route_table_id=route_table_id,
                                             opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_security_group(name,
                              description: Optional[str] = None,
                              vpc_id: Optional[str] = None,
                              tags: Optional[Mapping[str, str]] = None,
                              depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2securitygroup-" + name

        return aws.ec2.SecurityGroup(resource_name, description=description, name=name, tags=tags,
                                     vpc_id=vpc_id, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_sg_rule(name, security_group_id, from_port, to_port, protocol, rule_type,
                       description: Optional[str] = None,
                       cidr_blocks: Optional[Sequence[str]] = None,
                       is_self: Optional[bool] = None,
                       source_security_group_id: Optional[str] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2sgrule-" + name

        return aws.ec2.SecurityGroupRule(resource_name,
                                         cidr_blocks=cidr_blocks,
                                         description=description,
                                         from_port=from_port,
                                         protocol=protocol,
                                         security_group_id=security_group_id,
                                         source_security_group_id=source_security_group_id,
                                         self=is_self,
                                         to_port=to_port,
                                         type=rule_type,
                                         opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def get_security_group(name):
        return aws.ec2.get_security_group(name=name)

    @staticmethod
    def create_elastic_ip(name,
                          instance: Optional[str] = None,
                          vpc: Optional[bool] = False,
                          tags: Optional[Mapping[str, str]] = None,
                          depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2elasticip-" + name

        return aws.ec2.Eip(resource_name, instance=instance,
                           tags=tags, vpc=vpc, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_nat_gateway(name, allocation_id, subnet_id,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "ec2natgateway-" + name

        return aws.ec2.NatGateway(resource_name, allocation_id=allocation_id,
                                  subnet_id=subnet_id, tags=tags,
                                  opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_vpc_endpoint(name, vpc_id, service_name,
                            auto_accept: Optional[bool] = None,
                            policy: Optional[str] = None,
                            private_dns_enabled: Optional[bool] = None,
                            route_table_ids: Optional[Sequence[str]] = None,
                            security_group_ids: Optional[Sequence[str]] = None,
                            subnet_ids: Optional[Sequence[str]] = None,
                            vpc_endpoint_type: Optional[str] = None,
                            tags: Optional[Mapping[str, str]] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "vpcendpoint-" + name

        return aws.ec2.VpcEndpoint(resource_name, auto_accept=auto_accept,
                                   policy=policy, private_dns_enabled=private_dns_enabled,
                                   route_table_ids=route_table_ids, security_group_ids=security_group_ids,
                                   service_name=service_name, subnet_ids=subnet_ids, tags=tags,
                                   vpc_endpoint_type=vpc_endpoint_type, vpc_id=vpc_id,
                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_vpc_endpoint_route_table_association(name, route_table_id, vpc_endpoint_id,
                                                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "vpcendpointroutetableassociation-" + name

        return aws.ec2.VpcEndpointRouteTableAssociation(resource_name,
                                                        route_table_id=route_table_id,
                                                        vpc_endpoint_id=vpc_endpoint_id,
                                                        opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_network_acl(name, vpc_id,
                           subnet_ids: Optional[Sequence[str]] = None,
                           egress: Optional[Sequence[Input[InputType['NetworkAclEgressArgs']]]] = None,
                           ingress: Optional[Sequence[Input[InputType['NetworkAclIngressArgs']]]] = None,
                           tags: Optional[Mapping[str, str]] = None,
                           depends_on: Optional[Sequence[object]] = None):
        resource_name = "networkacl-" + name

        return aws.ec2.NetworkAcl(resource_name=resource_name, vpc_id=vpc_id, subnet_ids=subnet_ids,
                                  egress=egress, ingress=ingress, tags=tags,
                                  opts=ResourceOptions(depends_on=depends_on))
