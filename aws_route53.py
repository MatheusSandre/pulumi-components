from typing import Optional, Sequence, Mapping
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions

class Route53:
    @staticmethod
    def create_record(name, record_type, zone_id,
                      records: Optional[Sequence[str]] = None,
                      resource_name: Optional[Sequence[str]] = None,
                      aliases: Optional[Sequence[Input[InputType['RecordAliasArgs']]]] = None,
                      ttl: Optional[int] = None,
                      should_import: Optional[bool] = False,
                      depends_on: Optional[Sequence[object]] = None):
        if resource_name:
            resource_name = "route53record-" + resource_name
        else:
            resource_name = "route53record-" + name

        if should_import:
            record = aws.route53.Record(resource_name, name=name, records=records, aliases=aliases, ttl=ttl, type=record_type,
                                        zone_id=zone_id, opts=ResourceOptions(depends_on=depends_on,
                                                                              import_=f"{zone_id}_{name}_{record_type}"))
        else:
            record = aws.route53.Record(resource_name, name=name, records=records, aliases=aliases, ttl=ttl, type=record_type,
                                        zone_id=zone_id, opts=ResourceOptions(depends_on=depends_on))
        return record

    @staticmethod
    def create_zone(name,
                    comment: Optional[str] = None,
                    vpcs: Optional[Sequence["ZoneVpcArgs"]] = None,
                    tags: Optional[Mapping[str, str]] = None,
                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "route53zone-" + name

        return aws.route53.Zone(resource_name,
                                name=name, comment=comment, vpcs=vpcs, tags=tags,
                                opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_health_check(name,
                            failure_threshold: Optional[int] = None,
                            measure_latency: Optional[bool] = None,
                            port: Optional[int] = None,
                            request_interval: Optional[int] = None,
                            resource_path: Optional[str] = None,
                            tags: Optional[Mapping[str, str]] = None,
                            protocol: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):

        resource_name = "route53healthcheck-" + name

        return aws.route53.HealthCheck(resource_name,
                                       fqdn=name, failure_threshold=failure_threshold, measure_latency=measure_latency,
                                       port=port, request_interval=request_interval, resource_path=resource_path,
                                       tags=tags, type=protocol, opts=ResourceOptions(depends_on=depends_on))
