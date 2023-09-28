from typing import Optional, Mapping, Sequence

import pulumi_aws as aws

from pulumi import ResourceOptions

class ServiceDiscovery:
    @staticmethod
    def create_private_namespace(name,
                                 vpc_id,
                                 tags: Optional[Mapping[str, str]] = None):

        resource_name = "srv-discovery-private-namespace-" + name

        return aws.servicediscovery.PrivateDnsNamespace(resource_name,
                                                        name=name,
                                                        tags=tags,
                                                        vpc=vpc_id)

    @staticmethod
    def create_service(name,
                       namespace_id,
                       tags: Optional[Mapping[str, str]] = None,
                       depends_on: Optional[Sequence[object]] = None):
        resource_name = "sevicediscovery-service-" + name

        return aws.servicediscovery.Service(resource_name,
                                            name=name,
                                            dns_config=aws.servicediscovery.ServiceDnsConfigArgs(
                                                dns_records=[aws.servicediscovery.ServiceDnsConfigDnsRecordArgs(
                                                    ttl=10,
                                                    type="A",
                                                )],
                                                namespace_id=namespace_id,
                                            ),
                                            tags=tags,
                                            opts=ResourceOptions(depends_on=depends_on))
