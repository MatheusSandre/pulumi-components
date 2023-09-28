import unittest
import pulumi

from components.cloudflare_dns import DNS

class Mocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + '_id', args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}

pulumi.runtime.set_mocks(Mocks())

class TestingCloudflareDNSRecord(unittest.TestCase):
    @pulumi.runtime.test
    def setUp(self):
        self.record = DNS.create_record(
            name="www",
            zone_id="my_zone_id",
            value="192.168.1.1",
            record_type="A",
            proxied=True
        )

    @pulumi.runtime.test
    def test_name(self):
        def check_name(args):
            urn, name = args
            self.assertEqual(
                name, "www", f"Cloudflare DNS record name {urn} name must be 'www'")

        return pulumi.Output.all(self.record.urn, self.record.name).apply(check_name)

    @pulumi.runtime.test
    def test_zone_id(self):
        def check_zone_id(args):
            urn, zone_id = args
            self.assertEqual(
                zone_id, "my_zone_id", f"Cloudflare DNS record zone_id {urn} zone_id must be 'my_zone_id'")

        return pulumi.Output.all(self.record.urn, self.record.zone_id).apply(check_zone_id)

    @pulumi.runtime.test
    def test_value(self):
        def check_value(args):
            urn, value = args
            self.assertEqual(
                value, "192.168.1.1", f"Cloudflare DNS record value {urn} value must be '192.168.1.1'")

        return pulumi.Output.all(self.record.urn, self.record.value).apply(check_value)

    @pulumi.runtime.test
    def test_record_type(self):
        def check_record_type(args):
            urn, record_type = args
            self.assertEqual(
                record_type, "A", f"Cloudflare DNS record record_type {urn} record_type must be 'A'")

        return pulumi.Output.all(self.record.urn, self.record.type).apply(check_record_type)

    @pulumi.runtime.test
    def test_proxied(self):
        def check_proxied(args):
            urn, proxied = args
            self.assertEqual(
                proxied, True, f"Cloudflare DNS record proxied {urn} proxied must be boolean")

        return pulumi.Output.all(self.record.urn, self.record.proxied).apply(check_proxied)
