import json
import sys
import traceback
import yaml
import click

from lib import computes_info
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("summary")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--type", "server_type", type=click.Choice(['all', 'blade', 'rack'], case_sensitive=False), default='all', show_default=True)
@click.option("--column", "-c", default='default', help="Extra summary: all,fw,pci,fan,psu,storage")
@click.option("--loc", "locator", is_flag=True, default=False, help="Locator LED on")
@click.option("--off", "power_off", is_flag=True, default=False, help="Filter powered off")
@click.option("--health", is_flag=True, default=False, help="Filter unhealthy")
@click.option("--fan", is_flag=True, default=False, help="Filter unhealthy fans")
@click.option("--psu", is_flag=True, default=False, help="Filter unhealthy psu")
@click.option("--ucsm", is_flag=True, default=False, help="Filter UCSM managed")
@click.option("--standalone", is_flag=True, default=False, help="Filter standalone servers")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--pci", "pci_filter", default='', help="Pci model loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
@click.option("--cpu", "cpu_filter", default='', callback=validations.validate_int_oper, help="CPU cores filter")
@click.option("--memory", "memory_filter", default='', callback=validations.validate_int_oper, help="Memory [GiB] filter")
@click.option("--days", default=1, help="Last <n> days workflows")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_summary_command(
        ctx,
        iaccount,
        group,
        server_type,
        column,
        locator,
        power_off,
        health,
        fan,
        psu,
        ucsm,
        standalone,
        ip_filter,
        name_filter,
        model_filter,
        pci_filter,
        serial_filter,
        cpu_filter,
        memory_filter,
        days,
        output,
        devel
        ):
    """Get servers summary"""

    # iservers get summary

    ctx.developer = devel

    try:
        settings = {}
        settings['locator'] = True
        settings['workflow'] = 86400 * days
        settings['rack'] = True
        settings['blade'] = True
        if server_type.lower() == 'blade':
            settings['rack'] = False
        if server_type.lower() == 'rack':
            settings['blade'] = False

        # Selected columns for state gathering

        settings['cpu'] = False
        settings['memory'] = False

        for key in ['id', 'group', 'server_setting_id']:
            settings[key] = False

        if column == 'all':
            for key in ['fw', 'pci', 'fan', 'psu', 'storage']:
                settings[key] = True
        else:
            for key in ['fw', 'pci', 'fan', 'psu', 'storage']:
                settings[key] = False
                if key in column.split(','):
                    settings[key] = True

        # Server filtering options

        match_rules = {}
        match_rules['name'] = name_filter
        match_rules['model'] = model_filter
        match_rules['ip'] = ip_filter
        match_rules['serials'] = group
        if len(serial_filter) > 0:
            match_rules['serials'] = serial_filter
        match_rules['locator'] = locator
        match_rules['power_off'] = power_off
        match_rules['alarms'] = health
        match_rules['ucsm'] = ucsm
        match_rules['standalone'] = standalone
        match_rules['cpu'] = cpu_filter
        match_rules['memory'] = memory_filter
        match_rules['pci'] = pci_filter
        match_rules['fan'] = fan
        match_rules['psu'] = psu

        computes_handler = computes_info.ComputesInfo(iaccount, settings)
        servers = computes_handler.get(match_rules=match_rules)
        summary = computes_handler.get_summary(servers)

        ctx.my_output.json_output(servers)

        if output == 'json':
            ctx.my_output.default(json.dumps(summary, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                summary,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        computes_handler.print_summary(summary)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
