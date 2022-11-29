import click

from menu.delete.redfish.cache import delete_redfish_cache_command


class Failure(Exception):
    pass


@click.group("redfish")
@click.pass_obj
def delete_redfish_menu(ctx):
    """Delete redfish commands"""


delete_redfish_menu.add_command(delete_redfish_cache_command)
