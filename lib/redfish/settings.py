import os
import json
import traceback

from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class RedfishSettings(Settings):
    def __init__(self):
        Settings.__init__(self)
        self.log = log_helper.Log()
        self.my_output = output_helper.OutputHelper(
            verbose=False,
            debug=False
        )

        self.redfish_settings_filename = os.path.join(
            self.settings_dir,
            'redfish'
        )

        if not self.initialize_redfish_settings():
            raise ValueError('Redfish settings initialization failed')

    def get_redfish_settings(self):
        if not os.path.isfile(self.redfish_settings_filename):
            return None

        try:
            with open(self.redfish_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_redfish_settings', traceback.format_exc())
            return None

        return settings

    def set_redfish_settings(self, settings):
        try:
            with open(self.redfish_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_redfish_settings', traceback.format_exc())
            return False

        return True

    def get_redfish_default_settings(self):
        settings = {}
        settings['CacheEnabled'] = False
        settings['CacheDirectory'] = '/tmp/redfish'
        return settings

    def initialize_redfish_settings(self):
        if not os.path.isfile(self.redfish_settings_filename):
            settings = self.get_redfish_default_settings()
            if not self.set_redfish_settings(settings):
                return False
        return True

    def print_redfish_settings(self):
        settings = self.get_redfish_settings()
        if settings is None:
            self.my_output.error('Redfish settings not found')
            return

        order = [
            'CacheEnabled',
            'CacheDirectory'
        ]

        headers = [
            'Cache Enabled',
            'Cache Directory'
        ]

        self.my_output.dictionary(
            settings,
            title='Redfish Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
