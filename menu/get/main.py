import click

from menu.get.redfish.main import get_redfish_menu
from menu.get.ucsm.main import get_ucsm_menu
from menu.get.server import get_server_command
from menu.get.servers import get_servers_command
from menu.get.power import get_power_command
from menu.get.thermal import get_thermal_command
from menu.get.chassis import get_chassis_command
from menu.get.chassiz import get_chassiz_command
from menu.get.summary import get_summary_command
from menu.get.scu import get_scu_command
from menu.get.os_image import get_os_image_command
from menu.get.os_vendor import get_os_vendor_command
from menu.get.os_version import get_os_version_command
from menu.get.os_config import get_os_config_command
from menu.get.workflows import get_workflows_command
from menu.get.workflow import get_workflow_command


class Failure(Exception):
    pass


@click.group("get")
@click.pass_obj
def get_menu(ctx):
    """Get commands"""


get_menu.add_command(get_redfish_menu)
get_menu.add_command(get_ucsm_menu)
get_menu.add_command(get_server_command)
get_menu.add_command(get_servers_command)
get_menu.add_command(get_power_command)
get_menu.add_command(get_thermal_command)
get_menu.add_command(get_chassis_command)
get_menu.add_command(get_chassiz_command)
get_menu.add_command(get_summary_command)
get_menu.add_command(get_scu_command)
get_menu.add_command(get_os_image_command)
get_menu.add_command(get_os_vendor_command)
get_menu.add_command(get_os_version_command)
get_menu.add_command(get_os_config_command)
get_menu.add_command(get_workflows_command)
get_menu.add_command(get_workflow_command)
