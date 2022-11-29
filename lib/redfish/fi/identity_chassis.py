import uuid

from lib import ip_helper


class RedfishEndpointFabricInterconnectTemplateIdentityChassis():
    def __init__(self):
        self.identity_main_url = '/'
        self.identity_chassis_url = '/Chassis/1'

    def get_identity_chassis_default_cache_name(self, properties):
        name = 'chassis-%s-%s' % (
            properties['Product'],
            properties['SerialNumber'].lower()
        )
        return name

    def get_template_identity_chassis_properties(self):
        main = self.get_properties(self.identity_main_url)
        chassis = self.get_properties(self.identity_chassis_url)

        if main is None or chassis is None:
            return None

        properties = {}
        properties['Product'] = chassis['Model']
        properties['Model'] = chassis['Model']
        properties['Vendor'] = chassis['Manufacturer']
        properties['RedfishVersion'] = main['RedfishVersion']
        properties['SerialNumber'] = chassis['SerialNumber']
        properties['PowerState'] = 'Off'
        if self.is_chassis_power_on():
            properties['PowerState'] = 'On'
        properties['HostName'] = None
        properties['UUID'] = ip_helper.generate_uuid(
            properties['SerialNumber']
        )
        properties['Name'] = None

        properties['DefaultCacheName'] = self.get_identity_chassis_default_cache_name(properties)
        properties['CacheFileName'] = properties['UUID'].lower()

        return properties

    def print_template_identity_chassis_properties(self, properties):
        keys = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'HostName',
            'SerialNumber',
            'UUID',
            'BiosVersion',
            'Firmware',
            'PowerState',
            'RedfishVersion'
        ]

        headers = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'Hostname',
            'Serial Number',
            'UUID',
            'Bios Version',
            'Firmware',
            'Power State',
            'Redfish Version'
        ]

        self.my_output.dictionary(
            properties,
            title='UCS Rack Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        if self.endpoint_handler.is_cache_enabled():
            keys = [
                'DefaultCacheName',
                'CacheFileName'
            ]

            headers = [
                'DefaultCacheName',
                'CacheFileName'
            ]

            self.my_output.dictionary(
                properties,
                title='Redfish Endpoint Cache Settings',
                underline=True,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=headers
            )
