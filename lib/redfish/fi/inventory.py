import json


class RedfishEndpointFabricInterconnectInventory():
    def __init__(self):
        self.inventory_type = ''
        self.inventory_id = ''

    def get_inventory_type(self):
        return self.inventory_type

    def get_inventory_id(self):
        return self.inventory_id

    def set_inventory(self, inventory_type, inventory_id):
        self.inventory_type = inventory_type
        self.inventory_id = inventory_id

    def print_inventory_chassis(self, chassis):
        order = [
            'InventoryType',
            'Identifier',
            'Iom1',
            'Iom2',
            'Name',
            'Model',
            'Serial'
        ]

        headers = [
            'Inventory Type',
            'Chassis Id',
            'Inventory Id (IOM1)',
            'Inventory Id (IOM2)',
            'Chassis Name',
            'Chassis Model',
            'Chassis Serial',
        ]

        self.my_output.my_table(
            chassis,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_inventory_servers(self, servers):
        order = [
            'InventoryType',
            'Name',
            'ChassisIdentifier',
            'Model',
            'Serial'
        ]

        headers = [
            'Inventory Type',
            'Inventory Id',
            'Chassis Id',
            'Server Model',
            'Server Serial'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_inventory(self, inventory, output):
        if output == 'json':
            self.my_output.default(
                json.dumps(
                    inventory,
                    indent=4
                )
            )
            return

        self.print_inventory_chassis(inventory['chassis'])
        self.print_inventory_servers(inventory['servers'])

    def get_chassis_info(self, data):
        chassiz_info = []

        for chassis in data['Results']:
            chassis_info = {}
            chassis_info['InventoryType'] = 'Chassis'
            chassis_info['Iom1'] = chassis['Ioms'][0]['Name']
            chassis_info['Iom2'] = chassis['Ioms'][1]['Name']
            chassis_info['Name'] = chassis['chassis']['Name']
            chassis_info['Model'] = chassis['chassis']['Model']
            chassis_info['Serial'] = chassis['chassis']['Serial']
            chassis_info['Identifier'] = chassis['chassis']['Identifier']

            if chassis['chassis']['AlarmSummary']['Warning'] == 0 and chassis['chassis']['AlarmSummary']['Critical'] == 0:
                chassis_info['Health'] = 'Healthy'
                chassis_info['HealthSummary'] = 'Healthy'
            if chassis['chassis']['AlarmSummary']['Warning'] > 0 and chassis['chassis']['AlarmSummary']['Critical'] == 0:
                chassis_info['Health'] = 'Warnings'
                chassis_info['HealthSummary'] = 'Warnings (%s)' % (chassis['chassis']['AlarmSummary']['Warning'])
            if chassis['chassis']['AlarmSummary']['Critical'] > 0:
                chassis_info['Health'] = 'Critical'
                chassis_info['HealthSummary'] = 'Critical (%s)' % (chassis['chassis']['AlarmSummary']['Critical'])

            chassiz_info.append(chassis_info)

        return chassiz_info

    def get_servers_info(self, data):
        servers_info = []

        for server in data['Results']:
            server_info = {}
            server_info['InventoryType'] = 'Server'
            server_info['Name'] = server['Name']
            server_info['Model'] = server['Model']
            server_info['Serial'] = server['Serial']
            server_info['ConnectionStatus'] = server['ConnectionStatus']
            server_info['Identifier'] = server['Identifier']
            server_info['ChassisIdentifier'] = server['Identifier'].split('/')[0]

            server_info['OperPowerState'] = server['OperPowerState']
            server_info['Power'] = False
            if server_info['OperPowerState'] == 'on':
                server_info['Power'] = True
            server_info['ServerProfile'] = server['ServerProfile']

            server_info['IP_Inband'] = None
            server_info['IP_Outband'] = None
            for kvm in server['KvmIpAddresses']:
                if kvm['Name'] == 'Inband':
                    server_info['IP_Inband'] = kvm['Address']
                if kvm['Name'] == 'Outband':
                    server_info['IP_Outband'] = kvm['Address']

            if server['AlarmSummary']['Warning'] == 0 and server['AlarmSummary']['Critical'] == 0:
                server_info['Health'] = 'Healthy'
                server_info['HealthSummary'] = 'Healthy'
            if server['AlarmSummary']['Warning'] > 0 and server['AlarmSummary']['Critical'] == 0:
                server_info['Health'] = 'Warnings'
                server_info['HealthSummary'] = 'Warnings (%s)' % (server['AlarmSummary']['Warning'])
            if server['AlarmSummary']['Critical'] > 0:
                server_info['Health'] = 'Critical'
                server_info['HealthSummary'] = 'Critical (%s)' % (server['AlarmSummary']['Critical'])

            servers_info.append(server_info)

        return servers_info

    def get_server_to_chassis_info(self, inventory):
        for server in inventory['servers']:
            for chassis in inventory['chassis']:
                if server['ChassisIdentifier'] == chassis['Identifier']:
                    server['Chassis'] = chassis

        return inventory

    def get_server_inventory(self, server_system_id):
        inventory = self.get_inventory()

        for server in inventory['servers']:
            if server['Serial'] == server_system_id:
                return server

        return None

    def get_blades_id(self, inventory):
        blades = []

        for chassis in inventory['chassis']:
            chassis_properties = self.get_properties(
                'Chassis',
                fixup=True,
                inventory_type=chassis['InventoryType'],
                inventory_id=chassis['Iom1']
            )

            if chassis_properties is None:
                continue

            for member in chassis_properties['Members']:
                if member['@odata.id'].startswith('/redfish/v1/Chassis/Blade'):
                    blade = self.get_properties(
                        member['@odata.id'],
                        fixup=True,
                        inventory_type=chassis['InventoryType'],
                        inventory_id=chassis['Iom1']
                    )
                    if blade is not None:
                        if 'SerialNumber' in blade:
                            blade_info = {}
                            blade_info['ChassisId'] = chassis['Identifier']
                            blade_info['BladeId'] = blade['Id']
                            blade_info['SerialNumber'] = blade['SerialNumber']
                            blades.append(blade_info)

        return blades

    def get_server_to_blade_info(self, inventory):
        for server in inventory['servers']:
            server['BladeId'] = None

        blades = self.get_blades_id(inventory)
        if blades is None:
            return inventory

        for server in inventory['servers']:
            for blade in blades:
                if server['Serial'] == blade['SerialNumber']:
                    server['BladeId'] = blade['BladeId']

        return inventory

    def get_inventory(self):
        inventory = {}
        inventory['chassis'] = self.get_chassis_info(
            self.get_properties(
                'Chassis',
                fixup=False
            )
        )
        inventory['servers'] = self.get_servers_info(
            self.get_properties(
                'Servers',
                fixup=False
            )
        )

        inventory = self.get_server_to_chassis_info(inventory)
        inventory = self.get_server_to_blade_info(inventory)

        return inventory
