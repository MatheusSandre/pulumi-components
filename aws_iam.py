from typing import Optional, Mapping, Sequence
import pulumi_aws as aws

from pulumi import ResourceOptions

class IAM:

    @staticmethod
    def create_role(name,
                    role_statements,
                    description: Optional[str] = None,
                    max_session_duration: Optional[int] = None,
                    path: Optional[str] = None,
                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "iamrole-" + name

        policy = aws.iam.get_policy_document_output(statements=role_statements)

        return aws.iam.Role(resource_name, name=name, description=description, path=path,
                            assume_role_policy=policy.json, max_session_duration=max_session_duration,
                            opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_policy(name,
                                   statements,
                                   description: Optional[str] = None,
                                   path: Optional[str] = None,
                                   depends_on: Optional[Sequence[object]] = None):
        resource_name = "iampolicy-" + name

        policy = aws.iam.get_policy_document_output(statements=statements)

        return aws.iam.Policy(resource_name, name=name, description=description, path=path, policy=policy.json,
                              opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def attach_policy_into_role(resource_name, role, policy,
                                depends_on: Optional[Sequence[object]] = None):
        return aws.iam.RolePolicyAttachment(resource_name, role=role.name, policy_arn=policy,
                                            opts=ResourceOptions(protect=False, depends_on=depends_on))

    @staticmethod
    def get_policy(arn):
        return aws.iam.get_policy(arn=arn)

    @staticmethod
    def get_role(name):
        return aws.iam.get_role(name=name)

    @staticmethod
    def create_user(name,
                    path: Optional[str] = None,
                    permissions_boundary: Optional[str] = None,
                    force_destroy: Optional[bool] = None,
                    tags: Optional[Mapping[str, str]] = None,
                    depends_on: Optional[Sequence[object]] = None):
        resource_name = "iamuser-" + name

        return aws.iam.User(resource_name, force_destroy=force_destroy,
                            name=name, path=path, tags=tags,
                            permissions_boundary=permissions_boundary,
                            opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def attach_policy_into_user(resource_name, user, policy,
                                depends_on: Optional[Sequence[object]] = None):
        return aws.iam.UserPolicyAttachment(resource_name, user=user, policy_arn=policy.arn,
                                            opts=ResourceOptions(protect=False, depends_on=depends_on))

    @staticmethod
    def create_group(name,
                     path: Optional[str] = None,
                     depends_on: Optional[Sequence[object]] = None):
        resource_name = "iamgroup-" + name

        return aws.iam.Group(resource_name, name=name, path=path, opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def attach_policy_into_group(resource_name, group, policy,
                                 depends_on: Optional[Sequence[object]] = None):
        return aws.iam.GroupPolicyAttachment(resource_name, group=group, policy_arn=policy.arn,
                                             opts=ResourceOptions(protect=False, depends_on=depends_on))

    @staticmethod
    def add_user_into_group(resource_name, user, groups,
                            depends_on: Optional[Sequence[object]] = None):
        return aws.iam.UserGroupMembership(resource_name, groups=groups, user=user,
                                           opts=ResourceOptions(depends_on=depends_on))

    @staticmethod
    def create_instance_profile(name,
                                role: Optional[str] = None,
                                depends_on: Optional[Sequence[object]] = None):
        resource_name = "iaminstanceprofile-" + name

        return aws.iam.InstanceProfile(resource_name, name=name, role=role.name,
                                       opts=ResourceOptions(depends_on=depends_on))
