from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions

class Kinesis:
    @staticmethod
    def create_firehose_stream(name, destination,
                               s3_configuration: Optional[Input[
                                   InputType['FirehoseDeliveryStreamS3ConfigurationArgs']]] = None,
                               extended_s3_configuration: Optional[Input[
                                   InputType['FirehoseDeliveryStreamExtendedS3ConfigurationArgs']]] = None,
                               kinesis_source_configuration: Optional[Input[
                                   InputType['FirehoseDeliveryStreamKinesisSourceConfigurationArgs']]] = None,
                               elasticsearch_configuration: Optional[Input[
                                   InputType['FirehoseDeliveryStreamElasticsearchConfigurationArgs']]] = None,
                               tags: Optional[Mapping[str, str]] = None,
                               depends_on: Optional[Sequence[object]] = None):
        resource_name = "kinesisfirehosestream-" + name

        return aws.kinesis.FirehoseDeliveryStream(resource_name,
                                                  destination=destination,
                                                  s3_configuration=s3_configuration,
                                                  extended_s3_configuration=extended_s3_configuration,
                                                  kinesis_source_configuration=kinesis_source_configuration,
                                                  name=name,
                                                  elasticsearch_configuration=elasticsearch_configuration, tags=tags,
                                                  opts=ResourceOptions(depends_on=depends_on)
                                                  )

    @staticmethod
    def create_stream(name, shard_count,
                      retention_period: Optional[int] = None,
                      shard_level_metrics: Optional[Sequence[str]] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      depends_on: Optional[Sequence[object]] = None):
        resource_name = "kinesisstream-" + name

        return aws.kinesis.Stream(resource_name, name=name, retention_period=retention_period,
                                  shard_count=shard_count,
                                  shard_level_metrics=shard_level_metrics, tags=tags,
                                  opts=ResourceOptions(depends_on=depends_on))
