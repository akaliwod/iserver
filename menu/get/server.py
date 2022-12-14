import json
import sys
import time
import traceback
import threading
import yaml
import click

from lib.intersight import compute_info
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
@click.option("--power", is_flag=True, default=False, help="Show power consumption")
@click.option("--thermal", is_flag=True, default=False, help="Show thermal info")
@click.option("--power", is_flag=True, default=False, help="Show power consumption")
@click.option("--env", is_flag=True, default=False, help="Show environmental info")
@click.option("--all", "all_info", is_flag=True, default=False, help="Show all details")
@click.option("--days", default=7, type=click.INT, help="Last <n> days workflows")
@click.option("--legend", "legend_on", is_flag=True, show_default=True, default=False, help="Show legend")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
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
        power,
        thermal,
        env,
        all_info,
        days,
        legend_on,
        output,
        devel
        ):
    """Get server details"""

    # iwectl get server

    ctx.developer = devel

    try:
        if output not in ['json', 'yaml']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        server = common.get_selected_server(
            ctx,
            iaccount,
            name_filter,
            ip_filter,
            serial_filter,
            details=False,
            workflow=None,
            action=False,
            include_object=True
        )
        if server is None:
            raise ErrorExit

        if env:
            power = True
            thermal = True

        seconds = 86400 * days
        settings = common.get_server_selection_settings(details=False, workflow=seconds, action=False)
        settings['registration'] = True
        settings['locator'] = True
        settings['cpu'] = cpu or all_info
        settings['memory'] = memory or all_info
        settings['fw'] = firmware or all_info
        settings['pci'] = pci or all_info
        settings['fan'] = fan or all_info
        settings['psu'] = psu or all_info
        settings['storage'] = storage or all_info
        settings['power'] = power or all_info
        settings['thermal'] = thermal or all_info
        compute_handler = compute_info.ComputeInfo(iaccount, settings=settings, log_id=ctx.run_id)
        server_info = compute_handler.get_server_info(server['IntersightObject'])

        ctx.my_output.debug(
            json.dumps(server_info, indent=4)
        )

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

        ctx.my_output.json_output(server_info)

        compute_handler.print(
            server_info,
            legend_on=legend_on
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
