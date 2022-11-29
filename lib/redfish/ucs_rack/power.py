class RedfishEndpointUcsRackTemplatePower():
    def __init__(self):
        self.defult_power_uri = '/redfish/v1/Chassis/1/Power'

    def get_power_uri(self):
        chassis_uri = self.get_chassis_uri()
        children = self.endpoint_handler.get_odata_ids(chassis_uri)
        if children is None:
            self.log.error(
                'get_power_uri',
                'Failed to discover Power URI: %s' % (chassis_uri)
            )
            return self.defult_power_uri

        power_uri = None
        for child in children:
            if child == chassis_uri:
                continue

            leaf = child.split('/')[-1]
            if leaf == 'Power':
                power_uri = child
                break

        if power_uri is None:
            self.log.error(
                'get_power_uri',
                'Failed to find power uri: %s' % (chassis_uri)
            )
            return self.default_chassis_uri

        return power_uri

    def get_template_power_properties(self):
        uri = self.get_power_uri()
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['PowerControl'] = {}

        # {
        #     "PhysicalContext": "PowerSupply",
        #     "PowerMetrics": {
        #         "MinConsumedWatts": 186,
        #         "AverageConsumedWatts": 349,
        #         "MaxConsumedWatts": 495
        #     },
        #     "MemberId": "1",
        #     "PowerLimit": {
        #         "LimitException": "NoAction"
        #     },
        #     "PowerConsumedWatts": 360,
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerControl/1"
        # }
        power_control_data = data['PowerControl'][0]
        properties['PowerControl']['PowerConsumedWatts'] = power_control_data['PowerConsumedWatts']
        properties['PowerControl']['LimitException'] = 'N/A'
        if 'PowerLimit' in power_control_data:
            if 'LimitException' in power_control_data['PowerLimit']:
                properties['PowerControl']['LimitException'] = power_control_data['PowerLimit']['LimitException']
        if 'PowerMetrics' in power_control_data:
            for key in power_control_data['PowerMetrics']:
                properties['PowerControl'][key] = power_control_data['PowerMetrics'][key]

        # {
        #     "PhysicalContext": "PowerSupply",
        #     "SensorNumber": 48,
        #     "MemberId": "1",
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/PSU1_VOUT",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     },
        #     "UpperThresholdCritical": 14,
        #     "Name": "PSU1_VOUT",
        #     "ReadingVolts": 12.2
        # },
        properties['Voltage'] = []
        for voltage in data['Voltages']:
            voltage_info = {}

            keys = [
                'Name',
                'ReadingVolts',
                'UpperThresholdCritical',
                'PhysicalContext'
            ]
            for key in keys:
                voltage_info[key] = 'N/A'
                if key in voltage:
                    voltage_info[key] = voltage[key]

            keys = [
                'State',
                'Health'
            ]
            for key in keys:
                voltage_info[key] = 'N/A'
                if key in voltage['Status']:
                    voltage_info[key] = voltage['Status'][key]

            properties['Voltage'].append(voltage_info)

        # {
        #     "SerialNumber": "LIT241244RQ",
        #     "InputRanges": [
        #         {
        #             "InputType": "AC",
        #             "OutputWattage": 1050,
        #             "MaximumFrequencyHz": 63,
        #             "MaximumVoltage": 264,
        #             "MinimumVoltage": 90,
        #             "MinimumFrequencyHz": 47
        #         }
        #     ],
        #     "FirmwareVersion": "10062019",
        #     "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/PSU1",
        #     "PowerOutputWatts": 171,
        #     "LineInputVoltage": 229,
        #     "Name": "PSU1",
        #     "PowerInputWatts": 186,
        #     "Manufacturer": "Cisco Systems Inc",
        #     "LastPowerOutputWatts": 171,
        #     "MemberId": "1",
        #     "PartNumber": "341-0638-03",
        #     "PowerSupplyType": "AC",
        #     "Model": "PS-2112-9S-LF",
        #     "SparePartNumber": "341-0638-03",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     }
        # },
        properties['PowerSupply'] = []
        for power_supply in data['PowerSupplies']:
            power_supply_info = {}
            power_supply_info['Name'] = power_supply['Name']
            power_supply_info['Model'] = power_supply['Model']
            power_supply_info['SerialNumber'] = power_supply['SerialNumber']

            keys = [
                'PartNumber',
                'SparePartNumber',
                'Manufacturer',
                'FirmwareVersion',
                'PowerOutputWatts',
                'LastPowerOutputWatts',
                'PowerInputWatts',
                'PowerSupplyType'
            ]
            for key in keys:
                power_supply_info[key] = 'N/A'
                if key in power_supply:
                    power_supply_info[key] = power_supply[key]

            keys = [
                'State',
                'Health'
            ]
            for key in keys:
                power_supply_info[key] = 'N/A'
                if key in power_supply['Status']:
                    power_supply_info[key] = power_supply['Status'][key]

            for input_range in power_supply['InputRanges']:
                for key in input_range:
                    if key != 'InputType':
                        power_supply_info[key] = input_range[key]

            properties['PowerSupply'].append(power_supply_info)

        return properties

    def print_template_power_consumption_properties(self, properties):
        keys = [
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts',
            'LimitException'
        ]

        headers = [
            'Current',
            'Min',
            'Average',
            'Max',
            'Limit action'
        ]

        self.my_output.dictionary(
            properties['PowerControl'],
            title='Power Consumption (Watt)',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_power_voltage_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Name',
            'State',
            'Health',
            'Volts',
            'Upper Threshold'
        ]

        self.my_output.my_table(
            properties['Voltage'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'PowerOutputWatts',
            'PowerInputWatts',
            'MaximumVoltage',
            'MinimumVoltage',
            'MaximumFrequencyHz',
            'MinimumFrequencyHz'
        ]

        headers = [
            'Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (Watt)',
            'Max (V)',
            'Min (V)',
            'Max (Hz)',
            'Min (Hz)'
        ]

        self.my_output.my_table(
            properties['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_power_properties(self, properties):
        self.print_template_power_consumption_properties(properties)
        self.print_template_power_voltage_properties(properties)
        self.print_template_power_supply_properties(properties)
