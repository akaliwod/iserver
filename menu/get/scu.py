import json
import sys
import traceback
import click
import yaml

from lib import scu
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("scu")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml', 'set'], case_sensitive=False), default='default', show_default=True)
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify if link works")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_scu_command(ctx, iaccount, verify, output, devel):
    """Get software configuration utilities"""

    # iwectl get scu

    ctx.developer = devel

    try:
        scu_handler = scu.SoftwareConfigurationUtility(iaccount)
        scus = scu_handler.get_all()
        if output == 'json':
            ctx.my_output.default(json.dumps(scus, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                scus,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        if output == 'set':
            yaml_output = scu_handler.get_set_output(scus)
            if yaml_output is None:
                ctx.my_output.error('Failed to get set output type')
                raise ErrorExit

            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        scu_handler.print(scus, verify=verify)
        ctx.my_output.json_output(scus)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
