class RedfishEndpointUcsRackTemplateThermal():
    def __init__(self):
        self.defult_thermal_uri = '/redfish/v1/Chassis/1/Thermal'

    def get_thermal_uri(self):
        chassis_uri = self.get_chassis_uri()
        children = self.endpoint_handler.get_odata_ids(chassis_uri)
        if children is None:
            self.log.error(
                'get_thermal_uri',
                'Failed to discover thermal URI: %s' % (chassis_uri)
            )
            return self.defult_thermal_uri

        thermal_uri = None
        for child in children:
            if child == chassis_uri:
                continue

            leaf = child.split('/')[-1]
            if leaf == 'Thermal':
                thermal_uri = child
                break

        if thermal_uri is None:
            self.log.error(
                'get_thermal_uri',
                'Failed to find thermal uri: %s' % (chassis_uri)
            )
            return self.default_chassis_uri

        return thermal_uri

    def get_template_thermal_properties(self):
        uri = self.get_thermal_uri()
        data = self.get_properties(uri)
        if data is None:
            return None

        properties = {}
        properties['State'] = data['Status']['State']
        properties['Health'] = data['Status']['Health']

        # {
        #     "RelatedItem": [
        #         {
        #             "@odata.id": "/redfish/v1/Chassis/1"
        #         }
        #     ],
        #     "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Temperatures/MLOM_TEMP",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     },
        #     "SensorNumber": 60,
        #     "Name": "MLOM_TEMP",
        #     "PhysicalContext": "NetworkingDevice",
        #     "MemberId": "1",
        #     "UpperThresholdCritical": 90,
        #     "ReadingCelsius": 55
        # },
        properties['Temperature'] = []
        for sensor in data['Temperatures']:
            sensor_info = {}
            sensor_info['Name'] = sensor['Name']
            sensor_info['State'] = sensor['Status']['State']
            sensor_info['Health'] = sensor['Status']['Health']
            keys = [
                'SensorNumber',
                'PhysicalContext',
                'ReadingCelsius',
                'UpperThresholdCritical'
            ]
            for key in keys:
                sensor_info[key] = 'N/A'
                if key in sensor:
                    sensor_info[key] = sensor[key]

            properties['Temperature'].append(sensor_info)

        properties['Temperature'] = sorted(properties['Temperature'], key=lambda i: i['Name'])

        # {
        #     "RelatedItem": [
        #         {
        #             "@odata.id": "/redfish/v1/Chassis/1"
        #         }
        #     ],
        #     "@odata.id": "/redfish/v1/Chassis/1/Thermal#/Fans/MOD1_FAN1",
        #     "ReadingUnits": "RPM",
        #     "Reading": 7070,
        #     "PhysicalContext": "Fan",
        #     "MemberId": "1",
        #     "Name": "MOD1_FAN1_SPEED",
        #     "Status": {
        #         "State": "Enabled",
        #         "Health": "OK"
        #     }
        # },
        properties['Fan'] = []
        for fan in data['Fans']:
            fan_info = {}
            fan_info['Name'] = fan['Name']
            fan_info['State'] = fan['Status']['State']

            fan_info['Health'] = ''
            if 'Health' in fan['Status']:
                fan_info['Health'] = fan['Status']['Health']

            fan_info['PhysicalContext'] = ''
            if 'PhysicalContext' in fan:
                fan_info['PhysicalContext'] = fan['PhysicalContext']

            fan_info['ReadingUnits'] = ''
            if 'ReadingUnits' in fan:
                fan_info['ReadingUnits'] = fan['ReadingUnits']

            fan_info['Reading'] = ''
            if 'Reading' in fan:
                fan_info['Reading'] = fan['Reading']

            fan_info['Value'] = '%s %s' % (fan_info['Reading'], fan_info['ReadingUnits'])

            properties['Fan'].append(fan_info)

        properties['Fan'] = sorted(properties['Fan'], key=lambda i: i['Name'])

        return properties

    def print_template_thermal_summary_properties(self, properties):
        keys = [
            'State',
            'Health'
        ]

        headers = [
            'State',
            'Health'
        ]

        self.my_output.dictionary(
            properties,
            title='Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_template_thermal_temperature_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'PhysicalContext',
            'ReadingCelsius',
            'UpperThresholdCritical'
        ]

        headers = [
            'Name',
            'State',
            'Health',
            'Location',
            'Value (Celcius)',
            'Upper Threshold (Celcius)'
        ]

        self.my_output.my_table(
            properties['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_thermal_fan_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'Value'
        ]

        headers = [
            'Name',
            'State',
            'Health',
            'Value'
        ]

        self.my_output.my_table(
            properties['Fan'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_template_thermal_properties(self, properties):
        self.print_template_thermal_summary_properties(properties)
        self.print_template_thermal_temperature_properties(properties)
        self.print_template_thermal_fan_properties(properties)
