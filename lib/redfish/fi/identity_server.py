import uuid


class RedfishEndpointFabricInterconnectTemplateIdentityServer():
    def __init__(self):
        self.identity_main_url = '/'
        self.identity_system_url = '/Systems/SYSTEM_ID'
        self.identity_firmware_url = '/UpdateService/FirmwareInventory/CIMC'

    def get_identity_server_default_cache_name(self, properties):
        firmware = properties['Firmware']
        if len(firmware) > 0:
            firmware = firmware.replace('(', '.').replace(')', '')

        product = properties['Product'].replace('UCSC-', '').replace('UCSS-', '')

        name = 'ucsc-%s-%s-%s-%s' % (
            product.lower(),
            properties['SerialNumber'].lower(),
            firmware.lower(),
            properties['PowerState'].lower()
        )
        return name

    def get_template_identity_server_properties(self):
        main = self.get_properties(self.identity_main_url)
        system = self.get_properties(self.identity_system_url)
        firmware = self.get_properties(self.identity_firmware_url)

        if main is None or system is None or firmware is None:
            return None

        properties = {}
        properties['UUID'] = main['UUID']
        properties['RedfishVersion'] = main['RedfishVersion']
        properties['Product'] = system['Model']
        properties['Vendor'] = system['Manufacturer']

        if system is not None:
            keys = [
                'SerialNumber',
                'PowerState',
                'Name',
                'BiosVersion',
                'Model'
            ]
            for key in keys:
                properties[key] = ''
                if key in system:
                    properties[key] = system[key]

        properties['HostName'] = properties['Name']
        properties['Firmware'] = ''
        if firmware is not None:
            if 'Version' in firmware:
                properties['Firmware'] = firmware['Version']

        properties['DefaultCacheName'] = self.get_identity_server_default_cache_name(properties)
        if properties['UUID'] == '':
            properties['CacheFileName'] = str(uuid.uuid4()).lower()
        else:
            properties['CacheFileName'] = properties['UUID'].lower()

        return properties

    def print_template_identity_server_properties(self, properties):
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
            title='UCS FI-Attached Server Redfish Endpoint',
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
