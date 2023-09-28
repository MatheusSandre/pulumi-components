from typing import Optional, Mapping, Sequence
from pulumi import Input, InputType, ResourceOptions

import pulumi_aws as aws

class CodeStarNotification:
    @staticmethod
    def create_notification_rule(name,
                                 detail_type: Optional[str] = None,
                                 event_type_ids: Optional[Sequence[str]] = None,
                                 resource: Optional[str] = None,
                                 status: Optional[str] = None,
                                 tags: Optional[Mapping[str, str]] = None,
                                 targets: Optional[Sequence[Input[InputType['NotificationRuleTargetArgs']]]] = None,
                                 depends_on: Optional[Sequence[object]] = None):
        resourouce_name = "codestarnotification-" + name

        return aws.codestarnotifications.NotificationRule(resourouce_name,
                                                          name=name, detail_type=detail_type,
                                                          event_type_ids=event_type_ids, resource=resource,
                                                          status=status, tags=tags, targets=targets,
                                                          opts=ResourceOptions(depends_on=depends_on))
