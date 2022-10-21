import click

from menu.create.os_install.main import create_os_install_menu
from menu.create.scu import create_scu_command
from menu.create.os_image import create_os_image_command


class Failure(Exception):
    pass


@click.group("create")
@click.pass_obj
def create_menu(ctx):
    """Create commands"""


create_menu.add_command(create_os_install_menu)
create_menu.add_command(create_scu_command)
create_menu.add_command(create_os_image_command)
