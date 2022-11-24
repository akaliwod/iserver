import click

from menu.get.redfish.endpoint import get_redfish_endpoint_command
# from menu.get.redfish.chassis import get_redfish_server_command
# from menu.get.redfish.fi import get_redfish_server_command
# from menu.get.redfish.server import get_redfish_server_command
# from menu.get.redfish.servers import get_redfish_servers_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def get_redfish_menu(ctx):
    """Get redfish commands"""


get_redfish_menu.add_command(get_redfish_endpoint_command)
# get_redfish_menu.add_command(get_redfish_server_command)
# get_redfish_menu.add_command(get_redfish_servers_command)
