import click

from menu.set.power.on import set_power_on_command
from menu.set.power.off import set_power_off_command
from menu.set.power.cycle import set_power_cycle_command
from menu.set.power.hard import set_power_hard_command
from menu.set.power.shut import set_power_shut_command
from menu.set.power.reboot import set_power_reboot_command


class Failure(Exception):
    pass


@click.group("power")
@click.pass_obj
def set_power_menu(ctx):
    """Set power commands"""


set_power_menu.add_command(set_power_on_command)
set_power_menu.add_command(set_power_off_command)
set_power_menu.add_command(set_power_cycle_command)
set_power_menu.add_command(set_power_hard_command)
set_power_menu.add_command(set_power_shut_command)
set_power_menu.add_command(set_power_reboot_command)
