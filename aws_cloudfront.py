from typing import Optional, Sequence, Mapping
import pulumi_aws as aws

from pulumi import ResourceOptions

class Cloudfront:
    @staticmethod
    # pylint: disable=too-many-arguments
    def create_distribution(name, enabled, viewer_certificate, origins, default_cache_behavior, restrictions,
                            aliases: Optional[Sequence[str]] = None,
                            default_root_object: Optional[str] = None,
                            comment: Optional[str] = None,
                            price_class: Optional[str] = None,
                            ordered_cache_behaviors: Optional[Sequence[str]] = None,
                            custom_error_responses: Optional[Sequence[str]] = None,
                            logging_config: Optional[str] = None,
                            web_acl_id: Optional[str] = None,
                            is_ipv6_enabled: Optional[bool] = False,
                            tags: Optional[Mapping[str, str]] = None,
                            should_import: Optional[bool] = False,
                            distribution_id: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "cloudfrontdistribution-" + name

        if should_import:
            distribution = aws.cloudfront.Distribution(resource_name, aliases=aliases, comment=comment,
                                                       default_cache_behavior=default_cache_behavior,
                                                       enabled=enabled, is_ipv6_enabled=is_ipv6_enabled,
                                                       logging_config=logging_config, restrictions=restrictions,
                                                       ordered_cache_behaviors=ordered_cache_behaviors,
                                                       custom_error_responses=custom_error_responses,
                                                       default_root_object=default_root_object,
                                                       origins=origins, price_class=price_class, tags=tags,
                                                       viewer_certificate=viewer_certificate, web_acl_id=web_acl_id,
                                                       opts=ResourceOptions(ignore_changes=[],
                                                                            depends_on=depends_on,
                                                                            import_=distribution_id))
        else:
            distribution = aws.cloudfront.Distribution(resource_name, aliases=aliases, comment=comment,
                                                       default_cache_behavior=default_cache_behavior,
                                                       enabled=enabled, is_ipv6_enabled=is_ipv6_enabled,
                                                       logging_config=logging_config, restrictions=restrictions,
                                                       ordered_cache_behaviors=ordered_cache_behaviors,
                                                       custom_error_responses=custom_error_responses,
                                                       default_root_object=default_root_object,
                                                       origins=origins, price_class=price_class, tags=tags,
                                                       viewer_certificate=viewer_certificate, web_acl_id=web_acl_id,
                                                       opts=ResourceOptions(ignore_changes=[],
                                                                            depends_on=depends_on))

        return distribution

    @staticmethod
    def create_access_identity(name,
                               comment: Optional[str] = None,
                               depends_on: Optional[Sequence[object]] = None):
        resource_name = "cloudfrontaccessidentity-" + name

        return aws.cloudfront.OriginAccessIdentity(resource_name, comment=comment,
                                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def get_distribution(distribution_id):
        return aws.cloudfront.get_distribution(id=distribution_id)
