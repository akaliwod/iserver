import json
import time
import traceback
import requests

from lib.redfish.common import RedfishEndpointCommon
from lib.redfish.fi.inventory import RedfishEndpointFabricInterconnectInventory
from lib.redfish.fi.templates import RedfishEndpointFabricInterconnectTemplates

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class RedfishEndpointFabricInterconnect(RedfishEndpointCommon, RedfishEndpointFabricInterconnectInventory, RedfishEndpointFabricInterconnectTemplates):
    def __init__(self, endpoint_ip, endpoint_port, redfish_username, redfish_password, ssl_verify=False, deep_search_exlusions=True, verbose=False, debug=False):
        RedfishEndpointCommon.__init__(
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
        RedfishEndpointFabricInterconnectInventory.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplates.__init__(
            self
        )

        self.session_connected = False
        self.connect()

    def __del__(self):
        self.disconnect()

    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        uri = [
            '/api-explorer/resources/redfish/v1/JsonSchemas',
            '/api-explorer/resources/redfish/v1/TaskService'
        ]

        return uri

    def path_fixup(self, path):
        if path.startswith('/redfish/v1/'):
            path = path.lstrip('/redfish/v1/')

        if not path.startswith('/api-explorer/resources/redfish/v1'):
            path = '/api-explorer/resources/redfish/v1/%s' % (
                path.lstrip('/')
            )

        if 'SYSTEM_ID' in path:
            system_id = self.get_system_id()
            if system_id is None:
                self.log.error('get_properties', 'System ID not found')
                return None

            path = path.replace(
                'SYSTEM_ID',
                system_id
            )

        return path

    def get_properties(self, path, properties=[], fixup=True, inventory_type=None, inventory_id=None):
        if not self.is_connected():
            return None

        if fixup:
            path = self.path_fixup(path)

        start_time = int(time.time() * 1000)
        try:
            url = 'https://%s/%s' % (
                self.endpoint_ip,
                path
            )

            headers = {}
            if len(self.inventory_type) > 0 and len(self.inventory_id) > 0:
                headers['Inventory-Type'] = self.inventory_type
                headers['Inventory-Id'] = self.inventory_id

            if inventory_type is not None:
                headers['Inventory-Type'] = inventory_type

            if inventory_id is not None:
                headers['Inventory-Id'] = inventory_id

            response = self.session_handler.get(
                url,
                headers=headers,
                verify=self.ssl_verify
            )

        except BaseException:
            self.log.error(
                'get_properties',
                'Redfish get object exception: %s %s' % (self.endpoint_ip, path)
            )

            self.log.error(
                'get_properties',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                path,
                False,
                duration_ms
            )

            return None

        if response.status_code > 299:
            self.log.error(
                'get_properties',
                'Redfish get object failed: %s %s %s %s' % (
                    self.endpoint_ip,
                    path,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                path,
                False,
                duration_ms
            )

            return None

        try:
            all_properties = response.json()
        except BaseException:
            self.log.error(
                'get_properties',
                'Redfish get object json exception: %s %s' % (self.endpoint_ip, path)
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.redfish(
            path,
            True,
            duration_ms
        )

        if properties is None or len(properties) == 0:
            self.my_output.info('Redfish get %s in %s ms' % (path, duration_ms))
            self.log.odata(
                path,
                all_properties
            )
            return all_properties

        selected_properties = {}
        for key in properties:
            if key in all_properties:
                selected_properties[key] = all_properties[key]

        self.my_output.info('Redfish get %s in %s ms' % (path, duration_ms))
        self.log.odata(
            path,
            selected_properties
        )

        return selected_properties

    def is_connected(self):
        return self.session_connected

    def connect(self):
        if self.session_handler is not None:
            return True

        start_time = int(time.time() * 1000)
        self.session_handler = requests.Session()

        url = 'https://%s/Login' % (self.endpoint_ip)
        data = {}
        data['User'] = self.redfish_username
        data['Password'] = self.redfish_password

        try:
            response = self.session_handler.post(
                url,
                data=json.dumps(data),
                verify=self.ssl_verify
            )

        except BaseException:
            self.log.error(
                'connect',
                'Redfish authentication exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'connect',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'connect',
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'connect',
                'Redfish authentication failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'connect',
                False,
                duration_ms
            )

            return False

        self.log.debug(
            'connect',
            'Redfish authentication successful: %s' % (self.endpoint_ip)
        )
        self.log.debug(
            'connect',
            'Response headers: %s' % (str(response.headers))
        )

        self.session_connected = True

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.my_output.info('Redfish connected in %s ms' % (duration_ms))
        self.log.redfish(
            'connect',
            True,
            duration_ms
        )

        return True

    def disconnect(self):
        if self.session_handler is None:
            return True

        start_time = int(time.time() * 1000)
        url = 'https://%s/Logout' % (
            self.endpoint_ip
        )

        try:
            response = self.session_handler.post(
                url,
                verify=self.ssl_verify
            )
        except BaseException:
            self.log.error(
                'disconnect',
                'Redfish session close exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'disconnect',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'disconnect',
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'disconnect',
                'Redfish session close failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'disconnect',
                False,
                duration_ms
            )

            return False

        self.log.debug(
            'disconnect',
            'Redfish session close successful: %s' % (self.endpoint_ip)
        )

        self.session_connected = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.my_output.info('Redfish disconnected in %s ms' % (duration_ms))
        self.log.redfish(
            'disconnect',
            True,
            duration_ms
        )

        return True
