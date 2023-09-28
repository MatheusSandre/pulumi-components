from typing import Optional, Mapping, Sequence

import pulumi_aws as aws

from pulumi import ResourceOptions

class SNS:

    @staticmethod
    def create_topic(name,
                     display_name: Optional[str] = None,
                     tags: Optional[Mapping[str, str]] = None,
                     depends_on: Optional[Sequence[object]] = None):

        resource_name = "snstopic-" + name
        ignore_changes = ["lambda_success_feedback_sample_rate", "http_success_feedback_sample_rate",
                          "application_success_feedback_sample_rate", "sqs_success_feedback_sample_rate"]

        return aws.sns.Topic(resource_name, name=name, display_name=display_name, tags=tags,
                             opts=ResourceOptions(ignore_changes=ignore_changes, depends_on=depends_on))

    @staticmethod
    def create_acess_policy(name,
                            statements,
                            topic_arn: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):

        policy = aws.iam.get_policy_document_output(statements=statements)

        resource_name = "snsacesspolicy-" + name

        return aws.sns.TopicPolicy(resource_name,
                                   policy=policy.json,
                                   arn=topic_arn,
                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_subscription(name, topic, resource_type, resource, account_id, aws_region,
                            raw_message_enabled: Optional[bool] = False,
                            filter_policy: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):

        resource_name = "snssubscription-" + name

        if resource_type == "lambda":
            resource = f"function:{resource}"

        resource_endpoint = f"arn:aws:{resource_type}:{aws_region}:{account_id}:{resource}"
        topic_arn = f"arn:aws:sns:{aws_region}:{account_id}:{topic}"

        return aws.sns.TopicSubscription(resource_name,
                                         endpoint=resource_endpoint,
                                         protocol=resource_type,
                                         topic=topic_arn,
                                         raw_message_delivery=raw_message_enabled,
                                         filter_policy=filter_policy,
                                         opts=ResourceOptions(depends_on=depends_on))
