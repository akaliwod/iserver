from lib.redfish.standard.endpoint import RedfishEndpointStandard
from lib.redfish.hpe.template import RedfishEndpointHpeTemplate


class RedfishEndpointHpe(RedfishEndpointStandard, RedfishEndpointHpeTemplate):
    def __init__(self, endpoint_handler, endpoint_ip, endpoint_port, redfish_username, redfish_password, cache_filename=None, deep_search_exlusions=True, get_timeout=10, ssl_verify=False, verbose=False, debug=False):
        RedfishEndpointStandard.__init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            cache_filename=cache_filename,
            get_timeout=get_timeout,
            ssl_verify=ssl_verify,
            deep_search_exlusions=deep_search_exlusions,
            verbose=verbose,
            debug=debug
        )
        RedfishEndpointHpeTemplate.__init__(
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
