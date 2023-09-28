from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import ResourceOptions

class Cloudwatch:
    @staticmethod
    def create_log_group(name,
                         retention_in_days: Optional[int] = None,
                         tags: Optional[Mapping[str, str]] = None,
                         depends_on: Optional[Sequence[object]] = None):

        resource_name = "cloudwatchloggroup-" + name

        return aws.cloudwatch.LogGroup(resource_name, name=name,
                                       retention_in_days=retention_in_days, tags=tags,
                                       opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_event_rule(name,
                          description: Optional[str] = None,
                          is_enabled: Optional[bool] = None,
                          tags: Optional[Mapping[str, str]] = None,
                          schedule: Optional[str] = None,
                          event_pattern: Optional[str] = None,
                          depends_on: Optional[Sequence[object]] = None):
        resource_name = "cloudwatcheventrule-" + name

        return aws.cloudwatch.EventRule(resource_name, description=description, is_enabled=is_enabled,
                                        name=name, schedule_expression=schedule,
                                        tags=tags, event_pattern=event_pattern,
                                        opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_event_target(name, rule,
                            target_arn: Optional[str] = None,
                            target_input: Optional[str] = None,
                            role_arn: Optional[str] = None,
                            ecs_target: Optional[str] = None,
                            depends_on: Optional[Sequence[object]] = None):
        resource_name = "cloudwatcheventtarget-" + name

        return aws.cloudwatch.EventTarget(resource_name, arn=target_arn,
                                          input=target_input, role_arn=role_arn, ecs_target=ecs_target,
                                          rule=rule, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_alarm(name, comparison_operator, evaluation_periods,
                     description: Optional[str] = None,
                     alarm_actions: Optional[Sequence[str]] = None,
                     datapoints_to_alarm: Optional[int] = None,
                     dimensions: Optional[Mapping[str, str]] = None,
                     metric_name: Optional[str] = None,
                     metric_queries: Optional[Sequence[str]] = None,
                     namespace: Optional[str] = None,
                     period: Optional[int] = None,
                     statistic: Optional[str] = None,
                     threshold: Optional[float] = None,
                     tags: Optional[Mapping[str, str]] = None,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "cloudwatchalarm-" + name

        return aws.cloudwatch.MetricAlarm(resource_name, alarm_actions=alarm_actions,
                                          alarm_description=description, comparison_operator=comparison_operator,
                                          datapoints_to_alarm=datapoints_to_alarm, dimensions=dimensions,
                                          evaluation_periods=evaluation_periods, metric_name=metric_name,
                                          metric_queries=metric_queries, name=name, namespace=namespace,
                                          period=period, statistic=statistic, tags=tags, threshold=threshold,
                                          opts=ResourceOptions(depends_on=depends_on))
