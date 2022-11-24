import json
import time
import traceback
import requests

from lib.redfish.common import RedfishEndpointCommon

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class RedfishEndpointGeneric(RedfishEndpointCommon):
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

        self.connect()

    def __del__(self):
        self.disconnect()

    def extract_session_id(self, authentication_response):
        if 'Location' in authentication_response.headers:
            return authentication_response.headers['Location'].split('/')[-1]

        # {\n  "@odata.id":"/redfish/v1/SessionService/Sessions/5819",\n  "Description":"Session of user: admin",\n  "Name":"User Session #5819",\n  "Id":5819\n}
        try:
            content = json.loads(authentication_response.content.decode('utf-8'))
            return content['@odata.id'].split('/')[-1]
        except BaseException:
            pass

        return None

    def connect(self):
        if self.session_handler is not None:
            return True

        start_time = int(time.time() * 1000)
        self.session_handler = requests.Session()

        url = 'https://%s:%s/redfish/v1/SessionService/Sessions' % (self.endpoint_ip, self.endpoint_port)
        data = {}
        data['UserName'] = self.redfish_username
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
        self.log.debug(
            'connect',
            'Response content: %s' % (str(response.content))
        )

        self.session_id = self.extract_session_id(response)
        if self.session_id is None:
            self.my_output.error('Failed to get session_id from authentication response')
            return False

        self.session_token = response.headers['X-Auth-Token']

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
        url = 'https://%s:%s/redfish/v1/SessionService/Sessions/%s' % (
            self.endpoint_ip,
            self.endpoint_port,
            self.session_id
        )
        headers = {}
        headers['X-Auth-Token'] = self.session_token

        try:
            response = self.session_handler.delete(
                url,
                headers=headers,
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

        self.session_handler = None
        self.session_id = None
        self.session_token = None

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.my_output.info('Redfish disconnected in %s ms' % (duration_ms))
        self.log.redfish(
            'disconnect',
            True,
            duration_ms
        )

        return True
