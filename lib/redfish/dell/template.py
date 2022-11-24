from lib.redfish.dell.power import RedfishEndpointDellTemplatePower
from lib.redfish.dell.thermal import RedfishEndpointDellTemplateThermal


class RedfishEndpointDellTemplate(RedfishEndpointDellTemplatePower, RedfishEndpointDellTemplateThermal):
    def __init__(self):
        RedfishEndpointDellTemplatePower.__init__(
            self
        )
        RedfishEndpointDellTemplateThermal.__init__(
            self
        )

    def get_template_properties(self, template_name):
        if template_name.lower() == 'power':
            return self.get_template_power_properties()

        if template_name.lower() == 'thermal':
            return self.get_template_thermal_properties()

        self.my_output.error('Unsupported template: %s' % (template_name))
        self.my_output.default('Supported templates:')

        templates = ['power', 'temp']
        for template in templates:
            self.my_output.default('- %s' % (template))

        return None

    def print_template_properties(self, template_name, properties):
        if template_name.lower() == 'power':
            self.print_template_power_properties(properties)

        if template_name.lower() == 'thermal':
            self.print_template_thermal_properties(properties)
