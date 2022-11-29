import click

from menu.get.redfish.endpoint import get_redfish_endpoint_command
from menu.get.redfish.settings import get_redfish_settings_command
from menu.get.redfish.cache import get_redfish_cache_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def get_redfish_menu(ctx):
    """Get redfish commands"""


get_redfish_menu.add_command(get_redfish_endpoint_command)
get_redfish_menu.add_command(get_redfish_settings_command)
get_redfish_menu.add_command(get_redfish_cache_command)
