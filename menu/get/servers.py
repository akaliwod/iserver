import json
import sys
import traceback
import yaml
import click

from lib import computes_info
from lib import my_servers_helper
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("servers")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--type", "server_type", type=click.Choice(['all', 'blade', 'rack'], case_sensitive=False), default='all', show_default=True)
@click.option("--column", "-c", default='default', help="Extra columns: id,fw,pci,fan,psu,group,storage")
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
@click.option("--set", "set_group", default='', callback=validations.validate_group_oper, help="Set as group")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_servers_command(
        ctx,
        iaccount,
        group,
        server_type,
        column, locator,
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
        set_group,
        output,
        devel
        ):
    """Get servers list"""

    # iserver get servers list

    # Ideas
    # - mac search
    # - fw >= <= == !=
    # - what about oper state like temp??? or cpu vendor?
    # - workflow/tasks as flag (?)

    ctx.developer = devel

    try:
        settings = {}
        settings['locator'] = True
        settings['workflow'] = 86400
        settings['rack'] = True
        settings['blade'] = True
        if server_type.lower() == 'blade':
            settings['rack'] = False
        if server_type.lower() == 'rack':
            settings['blade'] = False

        # Selected columns for output

        for key in ['id', 'cpu', 'memory', 'fw', 'pci', 'fan', 'psu', 'group', 'storage', 'server_setting_id']:
            settings[key] = False
            if key in column.split(','):
                settings[key] = True

        # Make sure that columns choice follows filtering choice

        if len(pci_filter) > 0:
            settings['pci'] = True
        if fan:
            settings['fan'] = True
        if psu:
            settings['psu'] = True

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

        ctx.my_output.json_output(servers)

        if output == 'json':
            ctx.my_output.default(json.dumps(servers, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                servers,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        computes_handler.print(servers)

        # Set group operation handling

        if set_group is not None:
            my_servers_handler = my_servers_helper.MyServers()
            if set_group['oper'] == 'add':
                if my_servers_handler.add_group_servers(set_group['group'], servers):
                    ctx.my_output.default('Servers added to group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if set_group['oper'] == 'del':
                if my_servers_handler.del_group_servers(set_group['group'], servers):
                    ctx.my_output.default('Servers removed from group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if my_servers_handler.set_group_servers(set_group['group'], servers):
                ctx.my_output.default('Group configured with selected servers: %s' % (set_group['group']))
                return

            ctx.my_output.error('Failed to configure group with selected servers: %s' % (set_group['group']))
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
