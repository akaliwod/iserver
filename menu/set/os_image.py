import sys
import traceback
import click

from progress.bar import Bar

from lib import os_image
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("os-image")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Input yaml file")
@click.option("--id", "moid", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Id")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Name")
@click.option("--vendor", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Vendor")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Version")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="OS HTTP Link")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_os_image_command(ctx, filename, iaccount, moid, name, vendor, version, link, devel):
    """Set os image objects from input yaml file"""

    # iwectl set os-image

    ctx.developer = devel

    try:
        ctx.my_output.default('Input parameters verification...')

        if len(filename) > 0:
            images = validations.validate_yaml_file(ctx, filename)
            if images is None:
                raise ErrorExit

        if len(filename) == 0:
            images = []
            item = {}
            item['Moid'] = moid
            item['Name'] = name
            item['Vendor'] = vendor
            item['Version'] = version
            item['Link'] = link
            item['Type'] = 'url'
            images.append(item)

        image_handler = os_image.OsImage(iaccount)
        success, reason = image_handler.validate_set(images)
        if not success:
            ctx.my_output.error('Input parameters validation failed')
            ctx.my_output.default(reason)
            raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(images))
        bar_handler.goto(0)
        failed = []
        for item in images:
            if not image_handler.update(item['Moid'], item):
                failed.append(item['Moid'])
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some updates failed')
            for item in failed:
                ctx.my_output.default('- %s' % (item))
            raise ErrorExit

        images = image_handler.get_all()
        image_handler.print(images, verify=False)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
