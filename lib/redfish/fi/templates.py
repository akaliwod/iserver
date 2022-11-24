from lib.redfish.fi.power_chassis import RedfishEndpointFabricInterconnectTemplatePowerChassis
from lib.redfish.fi.power_server import RedfishEndpointFabricInterconnectTemplatePowerServer
from lib.redfish.fi.thermal_chassis import RedfishEndpointFabricInterconnectTemplateThermalChassis
from lib.redfish.fi.thermal_server import RedfishEndpointFabricInterconnectTemplateThermalServer


class RedfishEndpointFabricInterconnectTemplates(
    RedfishEndpointFabricInterconnectTemplatePowerChassis,
    RedfishEndpointFabricInterconnectTemplatePowerServer,
    RedfishEndpointFabricInterconnectTemplateThermalChassis,
    RedfishEndpointFabricInterconnectTemplateThermalServer
    ):
    def __init__(self):
        RedfishEndpointFabricInterconnectTemplatePowerChassis.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplatePowerServer.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplateThermalChassis.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplateThermalServer.__init__(
            self
        )

    def get_template_properties(self, template_name):
        if template_name.lower() == 'power':
            if self.inventory_type == 'Chassis':
                return self.get_template_power_chassis_properties()

            if self.inventory_type == 'Server':
                return self.get_template_power_server_properties()

        if template_name.lower() == 'thermal':
            if self.inventory_type == 'Chassis':
                return self.get_template_thermal_chassis_properties()

            if self.inventory_type == 'Server':
                return self.get_template_thermal_server_properties()

        self.my_output.error('Unsupported template: %s' % (template_name))
        self.my_output.default('Supported templates:')

        templates = ['power', 'temp']
        for template in templates:
            self.my_output.default('- %s' % (template))

        return None

    def print_template_properties(self, template_name, properties):
        if template_name.lower() == 'power':
            if self.inventory_type == 'Chassis':
                self.print_template_power_chassis_properties(properties)

            if self.inventory_type == 'Server':
                self.print_template_power_server_properties(properties)

        if template_name.lower() == 'thermal':
            if self.inventory_type == 'Chassis':
                self.print_template_thermal_chassis_properties(properties)

            if self.inventory_type == 'Server':
                self.print_template_thermal_server_properties(properties)
