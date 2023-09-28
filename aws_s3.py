from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions

class S3:
    @staticmethod
    def create_bucket(name,
                      lifecycle_rules: Optional[Sequence[Input[InputType['BucketLifecycleRuleArgs']]]] = None,
                      cors_rules: Optional[Sequence[Input[InputType['BucketCorsRuleArgs']]]] = None,
                      grants: Optional[Sequence[Input[InputType['BucketGrantArgs']]]] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      server_side_encryption_configuration: Optional[
                          Input[InputType['BucketServerSideEncryptionConfigurationArgs']]] = None,
                      website: Optional[Input[InputType['BucketWebsiteArgs']]] = None,
                      versioning: Optional[Input[InputType['BucketVersioningArgs']]] = None,
                      block_public_access: Optional[bool] = True,
                      # policy_configuration: Optional[Mapping[str, str]] = None,
                      depends_on: Optional[Sequence[object]] = None):

        record_name = "s3bucket-" + name

        bucket = aws.s3.Bucket(record_name, bucket=name,
                               lifecycle_rules=lifecycle_rules,
                               tags=tags, website=website, grants=grants,
                               cors_rules=cors_rules, versioning=versioning,
                               server_side_encryption_configuration=server_side_encryption_configuration,
                               opts=ResourceOptions(depends_on=depends_on))

        if block_public_access:
            aws.s3.BucketPublicAccessBlock("s3bucketpublicaccessblock-" + name,
                                           bucket=bucket.id,
                                           block_public_acls=True,
                                           block_public_policy=True,
                                           restrict_public_buckets=True,
                                           ignore_public_acls=True)

        return bucket

    @staticmethod
    def create_policy_bucket(bucket_name,
                             statements,
                             depends_on: Optional[Sequence[object]] = None):

        resource_name = "s3bucketpolicy-" + bucket_name
        policy = aws.iam.get_policy_document_output(statements=statements)

        return aws.s3.BucketPolicy(resource_name,
                                   bucket=bucket_name,
                                   policy=policy.json,
                                   opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_bucket_notification(name, bucket,
                                   lambda_functions: Optional[Sequence[
                                       Input[InputType['BucketNotificationLambdaFunctionArgs']]]] = None,
                                   queues: Optional[Sequence[Input[InputType['BucketNotificationQueueArgs']]]] = None,
                                   topics: Optional[Sequence[Input[InputType['BucketNotificationTopicArgs']]]] = None,
                                   depends_on: Optional[Sequence[object]] = None):
        resource_name = "s3bucketnotification-" + name

        return aws.s3.BucketNotification(resource_name, bucket=bucket,
                                         lambda_functions=lambda_functions,
                                         queues=queues, topics=topics,
                                         opts=ResourceOptions(depends_on=depends_on))
