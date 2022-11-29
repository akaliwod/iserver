import click

from menu.set.redfish.main import set_redfish_menu
from menu.set.power.main import set_power_menu
from menu.set.locator.main import set_locator_menu
from menu.set.scu import set_scu_command
from menu.set.os_image import set_os_image_command


class Failure(Exception):
    pass


@click.group("set")
@click.pass_obj
def set_menu(ctx):
    """Actions"""


set_menu.add_command(set_redfish_menu)
set_menu.add_command(set_power_menu)
set_menu.add_command(set_locator_menu)
set_menu.add_command(set_scu_command)
set_menu.add_command(set_os_image_command)
