from typing import Optional, Sequence

import pulumi_cloudflare as cloudflare
from pulumi import ResourceOptions

class DNS:

    @staticmethod
    def create_record(name,
                      zone_id,
                      record_type,
                      value,
                      proxied: Optional[bool] = None,
                      ttl: Optional[int] = None,
                      depends_on: Optional[Sequence[object]] = None
                      ):
        resource_name = "cloudflare-record-" + name

        return cloudflare.Record(resource_name, name=name, proxied=proxied,
                                 ttl=ttl, type=record_type, value=value, zone_id=zone_id,
                                 opts=ResourceOptions(depends_on=depends_on))
