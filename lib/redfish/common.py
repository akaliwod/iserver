import json
import time
import traceback
import requests

from lib import log_helper
from lib import output_helper

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class RedfishEndpointCommon():
    def __init__(self, endpoint_ip, endpoint_port, redfish_username, redfish_password, ssl_verify=False, deep_search_exlusions=True, verbose=False, debug=False):
        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            verbose=verbose,
            debug=debug
        )

        self.endpoint_ip = endpoint_ip
        self.endpoint_port = endpoint_port
        self.redfish_username = redfish_username
        self.redfish_password = redfish_password
        self.ssl_verify = ssl_verify

        self.system_id = None
        self.get_timeout = 10

        self.session_handler = None
        self.session_id = None
        self.session_token = None

        self.deep_search_exclusions = deep_search_exlusions

    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        uri = [
        ]
        return uri

    def is_connected(self):
        if self.session_id is not None and self.session_token is not None:
            return True
        return False

    def path_fixup(self, path):
        if not path.startswith('/redfish/v1/'):
            path = '/redfish/v1/%s' % (
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

    def get_property_keys(self, key):
        if '\'' in key:
            keys = []
            key_name = ''
            for item in key.split('.'):
                if item.startswith('"') and item.endswith('\''):
                    keys.append(item.strip('\''))
                    continue

                if item.startswith('\''):
                    key_name = item.lstrip('\'')
                    continue

                if item.endswith('\''):
                    key_name = '%s.%s' % (key_name, item.rstrip('\''))
                    keys.append(key_name)
                    key_name = ''
                    continue

                if key_name == '':
                    keys.append(item)
                    continue

                key_name = '%s.%s' % (key_name, item)

            return keys

        return key.split('.')

    def select_properties(self, data, properties):
        selected_properties = {}

        for property_value in properties:
            search_properties = data
            keys = self.get_property_keys(property_value)
            index = 0
            result = None

            for key in keys:
                index = index + 1
                if isinstance(search_properties, dict):
                    if key in search_properties:
                        search_properties = search_properties[key]
                        if index == len(keys):
                            result = search_properties
                            break

            if result is not None:
                selected_properties[property_value] = result

        return selected_properties

    def get_properties(self, path, properties=[]):
        if not self.is_connected():
            return None

        path = self.path_fixup(path)

        start_time = int(time.time() * 1000)
        try:
            url = 'https://%s:%s%s' % (
                self.endpoint_ip,
                self.endpoint_port,
                path
            )

            headers = {}
            headers['X-Auth-Token'] = self.session_token

            response = self.session_handler.get(
                url,
                headers=headers,
                verify=self.ssl_verify,
                timeout=self.get_timeout
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

        selected_properties = self.select_properties(
            all_properties,
            properties
        )
        self.my_output.info('Redfish get %s in %s ms' % (path, duration_ms))
        self.log.odata(
            path,
            selected_properties
        )

        return selected_properties

    def match_rule(self, rule, value):
        if rule.startswith('EQ('):
            if not isinstance(value, str):
                return False

            if value == rule.lstrip('EQ(').rstrip(')'):
                return True

            return False

        if rule.startswith('eq('):
            if isinstance(value, str):
                if value.lower() == rule.lstrip('eq(').rstrip(')').lower():
                    return True

            if isinstance(value, int):
                try:
                    if value == int(rule.lstrip('eq(').rstrip(')')):
                        return True
                except BaseException:
                    pass

            return False

        if rule.startswith('IN('):
            if not isinstance(value, str):
                return False

            if rule.lstrip('IN(').rstrip(')') in value:
                return True

            return False

        if rule.startswith('in('):
            if not isinstance(value, str):
                return False

            if rule.lstrip('in(').rstrip(')').lower() in value.lower():
                return True

            return False

        if rule.startswith('gt('):
            if not isinstance(value, int):
                try:
                    value = int(value)
                except BaseException:
                    return False

            try:
                if value > int(rule.lstrip('gt(').rstrip(')')):
                    return True
            except BaseException:
                pass

            return False

        if rule.startswith('ge('):
            if not isinstance(value, int):
                try:
                    value = int(value)
                except BaseException:
                    return False

            try:
                if value >= int(rule.lstrip('ge(').rstrip(')')):
                    return True
            except BaseException:
                pass

            return False

        if rule.startswith('lt('):
            if not isinstance(value, int):
                try:
                    value = int(value)
                except BaseException:
                    return False

            try:
                if value < int(rule.lstrip('lt(').rstrip(')')):
                    return True
            except BaseException:
                pass

            return False

        if rule.startswith('le('):
            if not isinstance(value, int):
                try:
                    value = int(value)
                except BaseException:
                    return False

            try:
                if value <= int(rule.lstrip('le(').rstrip(')')):
                    return True
            except BaseException:
                pass

            return False

        if rule.startswith('ne('):
            if isinstance(value, str):
                try:
                    if value.lower() != rule.lstrip('eq(').rstrip(')').lower():
                        return True
                except BaseException:
                    pass

            if isinstance(value, int):
                try:
                    if value != int(rule.lstrip('eq(').rstrip(')')):
                        return True
                except BaseException:
                    pass

            return False

        if rule.startswith('NE('):
            if isinstance(value, str):
                try:
                    if value != rule.lstrip('eq(').rstrip(')'):
                        return True
                except BaseException:
                    pass

            return False

        # implicit eq()
        if isinstance(value, str):
            if value.lower() == rule.lstrip('eq(').rstrip(')').lower():
                return True

        if isinstance(value, int):
            try:
                if value == int(rule.lstrip('eq(').rstrip(')')):
                    return True
            except BaseException:
                pass

        return False

    def match_rules(self, rules, value):
        # Match any
        for rule in rules:
            if self.match_rule(rule, value):
                return True

        return False

    def filter_key(self, data, rules):
        if not isinstance(data, dict):
            return data

        filtered = {}
        for key in data:
            if self.match_rules(rules, key):
                filtered[key] = data[key]
                continue

            if isinstance(data[key], dict):
                branch = self.filter_key(data[key], rules)
                if len(branch) > 0:
                    filtered[key] = branch

        return filtered

    def filter_value(self, data, rules):
        if not isinstance(data, dict):
            return data

        filtered = {}
        for key in data:
            if isinstance(data[key], dict):
                branch = self.filter_value(data[key], rules)
                if len(branch) > 0:
                    filtered[key] = branch
                continue

            if isinstance(data[key], list):
                continue

            if self.match_rules(rules, data[key]):
                filtered[key] = data[key]

        return filtered

    def get_system_id(self):
        if self.system_id is not None:
            return self.system_id

        value = self.get_properties('Systems')
        if value is None:
            return None

        try:
            system_id = value['Members'][0]['@odata.id'].split('/')[-1]
            self.system_id = system_id
        except BaseException:
            self.log.error(
                'get_system_id',
                json.dumps(value, indent=4)
            )
            return None

        return self.system_id
