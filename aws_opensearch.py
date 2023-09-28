from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import Input, InputType, ResourceOptions


class Opensearch:

    @staticmethod
    def create_domain(name,
                      engine_version: Optional[str] = None,
                      cluster_config: Optional[Input[InputType['DomainClusterConfigArgs']]] = None,
                      cognito_options: Optional[Input[InputType['DomainCognitoOptionsArgs']]] = None,
                      log_publishing_options: Optional[
                          Sequence[Input[InputType['DomainLogPublishingOptionArgs']]]] = None,
                      ebs_options: Optional[Input[InputType['DomainEbsOptionsArgs']]] = None,
                      vpc_options: Optional[Input[InputType['DomainVpcOptionsArgs']]] = None,
                      domain_endpoint_options: Optional[Input[InputType['DomainDomainEndpointOptionsArgs']]] = None,
                      advanced_security_options: Optional[Input[InputType['DomainAdvancedSecurityOptionsArgs']]] = None,
                      node_to_node_encryption: Optional[Input[InputType['DomainNodeToNodeEncryptionArgs']]] = None,
                      encrypt_at_rest: Optional[Input[InputType['DomainEncryptAtRestArgs']]] = None,
                      tags: Optional[Mapping[str, str]] = None,
                      depends_on: Optional[Sequence[object]] = None):
        resource_name = "opensearchdomain-" + name

        return aws.opensearch.Domain(resource_name,
                                     cluster_config=cluster_config, cognito_options=cognito_options,
                                     domain_endpoint_options=domain_endpoint_options, domain_name=name,
                                     ebs_options=ebs_options, engine_version=engine_version,
                                     log_publishing_options=log_publishing_options, vpc_options=vpc_options,
                                     tags=tags, advanced_security_options=advanced_security_options,
                                     node_to_node_encryption=node_to_node_encryption,
                                     encrypt_at_rest=encrypt_at_rest,
                                     opts=ResourceOptions(ignore_changes=[], depends_on=depends_on))

    @staticmethod
    def get_domain(name):
        return aws.opensearch.get_domain(domain_name=name)

    @staticmethod
    def create_policy(domain_name,
                      statements,
                      depends_on: Optional[Sequence[object]] = None):

        resource_name = "domainpolicy-" + domain_name
        policy = aws.iam.get_policy_document_output(statements=statements)

        return aws.opensearch.DomainPolicy(resource_name,
                                           access_policies=policy.json,
                                           domain_name=domain_name,
                                           opts=ResourceOptions(depends_on=depends_on))
