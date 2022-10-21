import click

from menu.set.locator.on import set_locator_on_command
from menu.set.locator.off import set_locator_off_command


class Failure(Exception):
    pass


@click.group("locator")
@click.pass_obj
def set_locator_menu(ctx):
    """Set locator commands"""


set_locator_menu.add_command(set_locator_on_command)
set_locator_menu.add_command(set_locator_off_command)
