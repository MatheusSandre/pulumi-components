from typing import Optional, Sequence

import pulumi_cloudflare as cloudflare
from pulumi import ResourceOptions


class PageRule:

    @staticmethod
    def create_page_rule(name,
                         zone_id,
                         target,
                         actions,
                         status,
                         priority: Optional[int] = None,
                         depends_on: Optional[Sequence[object]] = None
                         ):
        resource_name = "cloudflare-page-rule-" + name

        return cloudflare.PageRule(resource_name, actions=actions, priority=priority,
                                   status=status, target=target, zone_id=zone_id,
                                   opts=ResourceOptions(depends_on=depends_on))
