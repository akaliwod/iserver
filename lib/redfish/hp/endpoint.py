from lib.redfish.generic.endpoint import RedfishEndpointGeneric
from lib.redfish.hp.template import RedfishEndpointHpTemplate


class RedfishEndpointHp(RedfishEndpointGeneric, RedfishEndpointHpTemplate):
    def __init__(self, endpoint_ip, endpoint_port, redfish_username, redfish_password, deep_search_exlusions=True, ssl_verify=False, verbose=False, debug=False):
        RedfishEndpointGeneric.__init__(
            self,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            ssl_verify=ssl_verify,
            deep_search_exlusions=deep_search_exlusions,
            verbose=verbose,
            debug=debug
        )
        RedfishEndpointHpTemplate.__init__(
            self
        )

    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        uri = [
            '/redfish/v1/TelemetryService',
            '/redfish/v1/Managers/1/LogServices',
            '/redfish/v1/Systems/1/LogServices',
            '/redfish/v1/JsonSchemas',
            '/redfish/v1/UpdateService/SoftwareInventory',
            '/redfish/v1/SessionService/Sessions'
        ]

        return uri
