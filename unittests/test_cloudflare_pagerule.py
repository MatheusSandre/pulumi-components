import unittest
import pulumi

from components.cloudflare_pagerule import PageRule


class Mocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + '_id', args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


pulumi.runtime.set_mocks(Mocks())


class TestingCloudflarePageRule(unittest.TestCase):
    @pulumi.runtime.test
    def setUp(self):
        self.page_rule = PageRule.create_page_rule(
            name="my_rule",
            zone_id="my_zone_id",
            target="www.minhaurl.com.br/*",
            actions={
                "cache_level": "bypass"
            },
            status="active"
        )

    @pulumi.runtime.test
    def test_zone_id(self):
        def check_zone_id(args):
            urn, zone_id = args
            self.assertEqual(
                zone_id, "my_zone_id", f"Cloudflare Page Rule zone_id {urn} zone_id must be 'my_zone_id'")

        return pulumi.Output.all(self.page_rule.urn, self.page_rule.zone_id).apply(check_zone_id)

    @pulumi.runtime.test
    def test_target(self):
        def check_target(args):
            urn, target = args
            self.assertEqual(
                target, "www.minhaurl.com.br/*", f"Cloudflare Page Rule target {urn} target must be 'www.minhaurl.com.br/*'")

        return pulumi.Output.all(self.page_rule.urn, self.page_rule.target).apply(check_target)

    @pulumi.runtime.test
    def test_actions(self):
        def check_actions(args):
            urn, actions = args
            actions_rule = {
                "cache_level": "bypass"
            }
            self.assertEqual(
                actions, actions_rule, f"Cloudflare Page Rule actions {urn} actions must be a map")

        return pulumi.Output.all(self.page_rule.urn, self.page_rule.actions).apply(check_actions)

    @pulumi.runtime.test
    def test_status(self):
        def check_status(args):
            urn, status = args
            self.assertEqual(
                status, "active", f"Cloudflare Page Rule status {urn} status must be 'active'")

        return pulumi.Output.all(self.page_rule.urn, self.page_rule.status).apply(check_status)
