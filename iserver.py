import sys

from lib import output_helper
from lib import settings_helper
from lib import my_servers_helper
from lib import my_server_helper
from lib import iaccount_helper
from menu import main as menu_main


def initialize():
    my_output = output_helper.OutputHelper()

    isctl_success, isctl_output = menu_main.check_isctl()
    if not isctl_success:
        my_output.error('isctl command execution failed')
        my_output.default('\niserver requires isctl\n')
        my_output.default('Notes')
        my_output.default('- follow isctl installation instructions from https://github.com/cgascoig/isctl')
        my_output.default('- iserver runs \'isctl\' command')
        my_output.default('- make sure that isctl binary is in your $PATH e.g. /usr/local/bin/isctl')
        my_output.default('')
        return False

    settings_handler = settings_helper.Settings()
    if not settings_handler.initialize_settings():
        my_output.error('Local settings initialization failure...')
        return False

    my_servers = my_servers_helper.MyServers()
    if not my_servers.initialize():
        my_output.error('My servers settings initialization failure...')
        return False

    my_server = my_server_helper.MyServer()
    if not my_server.initialize():
        my_output.error('My server settings initialization failure...')
        return False

    iaccount_handler = iaccount_helper.IntersightAccount()
    if not iaccount_handler.is_isctl():
        my_output.error('isctl not found')
        return False

    if not iaccount_handler.is_isctl_configured():
        my_output.error('isctl not configured')
        my_output.default('\niserver requires isctl that is configured to work with Intersight\n')
        my_output.default('Notes')
        my_output.default('- follow isctl configuration instructions from https://github.com/cgascoig/isctl')
        my_output.default('- iserver expects $HOME/.isctl.yaml file with isctl configuration parameters')
        my_output.default('')
        return False

    if not iaccount_handler.initialize_iaccount():
        my_output.error('iaccount initialization failure')
        return False

    return True


if __name__ == "__main__":
    if not initialize():
        sys.exit(1)

    parameters = []
    for item in sys.argv:
        if len(item.split(' ')) == 1:
            parameters.append(item)
        else:
            parameters.append('"%s"' % (item))

    USER_INPUT = ' '.join(parameters)
    menu_main.run(USER_INPUT)
