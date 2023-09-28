from typing import Optional, Mapping, Sequence

import pulumi_aws as aws
from pulumi import ResourceOptions


class SQS:

    @staticmethod
    def create_queue(name,
                     message_retention_seconds: Optional[int] = None,
                     fifo_enabled: Optional[bool] = False,
                     tags: Optional[Mapping[str, str]] = None,
                     receive_wait_time_seconds: Optional[int] = None,
                     visibility_timeout_seconds: Optional[int] = None,
                     delay_seconds: Optional[int] = None,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "sqsqueue-" + name

        return aws.sqs.Queue(resource_name, name=name, fifo_queue=fifo_enabled, tags=tags,
                             message_retention_seconds=message_retention_seconds, delay_seconds=delay_seconds,
                             receive_wait_time_seconds=receive_wait_time_seconds,
                             visibility_timeout_seconds=visibility_timeout_seconds,
                             opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_redrive_policy(name,
                              queue_url: Optional[str] = None,
                              redrive_policy: Optional[str] = None,
                              depends_on: Optional[Sequence[object]] = None):
        resource_name = "sqsredrivepolicy-" + name

        return aws.sqs.RedrivePolicy(resource_name,
                                     queue_url=queue_url,
                                     redrive_policy=redrive_policy,
                                     opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_redrive_allow_policy(name,
                                    queue_url: Optional[str] = None,
                                    redrive_allow_policy: Optional[str] = None,
                                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "sqsredriveallowpolicy-" + name

        return aws.sqs.RedriveAllowPolicy(resource_name,
                                          queue_url=queue_url,
                                          redrive_allow_policy=redrive_allow_policy,
                                          opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_queue_policy(name,
                            queue_url: Optional[str] = None,
                            statements: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "sqspolicy-" + name

        policy = aws.iam.get_policy_document_output(
            statements=statements)

        return aws.sqs.Policy(resource_name,
                              queue_url=queue_url,
                              policy=policy.json,
                              opts=ResourceOptions(depends_on=depends_on))
