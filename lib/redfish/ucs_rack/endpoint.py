from lib.redfish.generic.endpoint import RedfishEndpointGeneric
from lib.redfish.ucs_rack.template import RedfishEndpointUcsRackTemplate


class RedfishEndpointUcsRack(RedfishEndpointGeneric, RedfishEndpointUcsRackTemplate):
    def __init__(self, endpoint_ip, endpoint_port, redfish_username, redfish_password, ssl_verify=False, deep_search_exlusions=True, verbose=False, debug=False):
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
        RedfishEndpointUcsRackTemplate.__init__(
            self
        )

    def get_excluded_tree_uri(self):
        system_id = self.get_system_id()

        uri = [
            '/redfish/v1/JsonSchemas',
            '/redfish/v1/Chassis/1/LogServices',
            '/redfish/v1/SessionService',
            '/redfish/v1/Managers/CIMC/LogServices',
            '/redfish/v1/Systems/%s/LogServices' % (system_id)
        ]

        return uri
