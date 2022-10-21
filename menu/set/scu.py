import sys
import traceback
import click

from progress.bar import Bar

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
@click.option("--filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Input yaml file")
@click.option("--id", "moid", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Id")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Name")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Version")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU HTTP Link")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_scu_command(ctx, filename, iaccount, moid, name, version, link, devel):
    """Set software configuration utilities"""

    # iwectl set scu

    ctx.developer = devel

    try:
        ctx.my_output.default('Input parameters verification...')

        if len(filename) > 0:
            scus = validations.validate_yaml_file(ctx, filename)
            if scus is None:
                raise ErrorExit

        if len(filename) == 0:
            scus = []
            item = {}
            item['Moid'] = moid
            item['Name'] = name
            item['Version'] = version
            item['Link'] = link
            item['Type'] = 'url'
            scus.append(item)

        scu_handler = scu.SoftwareConfigurationUtility(iaccount)
        success, reason = scu_handler.validate_set(scus)
        if not success:
            ctx.my_output.error('Input parameters validation failed')
            ctx.my_output.default(reason)
            raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(scus))
        bar_handler.goto(0)
        failed = []
        for item in scus:
            if not scu_handler.update(item['Moid'], item):
                failed.append(item['Moid'])
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some updates failed')
            for item in failed:
                ctx.my_output.default('- %s' % (item))
            raise ErrorExit

        scus = scu_handler.get_all()
        scu_handler.print(scus, verify=False)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
