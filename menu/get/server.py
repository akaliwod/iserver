import os
import json
import sys
import time
import traceback
import threading
import yaml
import click

from lib import compute_info
from menu import common
from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--serial", "serial_filter", default='', help="Serial number")
@click.option("--cpu", is_flag=True, default=False, help="Show processor units")
@click.option("--memory", is_flag=True, default=False, help="Show memory units")
@click.option("--fw", "firmware", is_flag=True, default=False, help="Show fw info")
@click.option("--fan", is_flag=True, default=False, help="Show fan units")
@click.option("--psu", is_flag=True, default=False, help="Show psu units")
@click.option("--storage", is_flag=True, default=False, help="Show storage details")
@click.option("--pci", is_flag=True, default=False, help="Show pci details")
@click.option("--all", "all_info", is_flag=True, default=False, help="Show all details")
@click.option("--days", default=7, type=click.INT, help="Last <n> days workflows")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--flat", is_flag=True, show_default=True, default=False, help="Flat output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_server_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
        cpu,
        memory,
        firmware,
        fan,
        psu,
        storage,
        pci,
        all_info,
        days,
        output,
        flat,
        devel
        ):
    """Get server details"""

    # iwectl get server

    ctx.developer = devel

    try:
        if output not in ['json', 'yaml']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        server = common.get_selected_server(ctx, iaccount, name_filter, ip_filter, serial_filter, details=False, workflow=None, action=False)
        if server is None:
            raise ErrorExit

        seconds = 86400 * days
        settings = common.get_server_selection_settings(details=False, workflow=seconds, action=False)
        settings['cpu'] = cpu or all_info
        settings['memory'] = memory or all_info
        settings['fw'] = firmware or all_info
        settings['pci'] = pci or all_info
        settings['fan'] = fan or all_info
        settings['psu'] = psu or all_info
        settings['storage'] = storage or all_info
        compute_handler = compute_info.ComputeInfo(iaccount, settings=settings)
        server_info = compute_handler.get(server=server)

        if output == 'json':
            ctx.my_output.default(json.dumps(server_info, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                server_info,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.busy = False
        time.sleep(.1)
        ctx.my_output.default('')
        if not flat and os.get_terminal_size()[0] > 80:
            compute_handler.print(server_info, multi_column=True)
        else:
            compute_handler.print(server_info, multi_column=False)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
