from lib.redfish.generic.endpoint import RedfishEndpointGeneric
from lib.redfish.dell.template import RedfishEndpointDellTemplate


class RedfishEndpointDell(RedfishEndpointGeneric, RedfishEndpointDellTemplate):
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
        RedfishEndpointDellTemplate.__init__(
            self
        )

    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        uri = [
            '/redfish/v1/Managers/iDRAC.Embedded.1/PrivilegeRegistry',
            '/redfish/v1/Systems/System.Embedded.1/SecureBoot/Oem/Dell/Certificates',
            '/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/Jobs',
            '/redfish/v1/JobService/Jobs',
            '/redfish/v1/Managers/iDRAC.Embedded.1/LogServices',
            '/redfish/v1/AccountService',
            '/redfish/v1/TelemetryService',
            '/redfish/v1/JsonSchemas',
            '/redfish/v1/UpdateService/FirmwareInventory',
            '/redfish/v1/UpdateService/SoftwareInventory',
            '/redfish/v1/Systems/System.Embedded.1/SecureBoot/SecureBootDatabases',
            '/redfish/v1/SessionService'
        ]

        return uri
