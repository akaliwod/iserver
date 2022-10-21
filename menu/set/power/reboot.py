import sys
import traceback
import click

from lib import lcm_server_power
from menu import defaults
from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("reboot")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial numbers")
@click.option("--name", "name_filter", default='', help="Name loose match")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait mode")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_power_reboot_command(ctx, iaccount, group, serial_filter, name_filter, ip_filter, no_confirm, no_wait, dry_run, verbose, devel):
    """CIMC reboot"""

    # iserver set power reboot

    ctx.developer = devel
    silent = False
    debug = False
    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        servers = common.get_selected_servers(ctx, iaccount, group, serial_filter, name_filter, ip_filter, not no_confirm)
        if servers is None or len(servers) == 0:
            raise ErrorExit

        lcm_server_power_handler = lcm_server_power.LcmServerPower(
            iaccount,
            dry_run=dry_run,
            wait=not no_wait,
            silent=silent,
            verbose=verbose,
            debug=debug
        )
        if not lcm_server_power_handler.power_reboot(servers):
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
