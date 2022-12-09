import sys
import traceback
import click

from progress.bar import Bar

from lib.intersight import os_image
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
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Name")
@click.option("--vendor", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Vendor")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="OS Version")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="OS HTTP Link")
@click.option("--organization", "organization_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Organization Name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_os_image_command(ctx, iaccount, filename, organization_name, name, vendor, version, link, devel):
    """Create os image"""

    # iserver create os-image

    ctx.developer = devel

    try:
        ctx.my_output.default('Input parameters verification...')

        if len(filename) > 0:
            images = validations.validate_yaml_file(ctx, filename)
            if images is None:
                raise ErrorExit

        if len(filename) == 0:
            organization_id = validations.validate_organization(ctx, iaccount, organization_name)
            if organization_id is None:
                raise ErrorExit

            if len(name) == 0:
                ctx.my_output.error('Define name')
                raise ErrorExit

            if len(vendor) == 0:
                ctx.my_output.error('Define vendor')
                raise ErrorExit

            if len(version) == 0:
                ctx.my_output.error('Define version')
                raise ErrorExit

            if len(link) == 0:
                ctx.my_output.error('Define link')
                raise ErrorExit

            images = []
            item = {}
            item['Name'] = name
            item['Vendor'] = vendor
            item['Version'] = version
            item['Link'] = link
            item['Type'] = 'url'
            item['Organization'] = organization_name
            images.append(item)

        image_handler = os_image.OsImage(iaccount, log_id=ctx.run_id)
        for image_definition in images:
            success, reason = image_handler.validate_add(image_definition)
            if not success:
                ctx.my_output.error('Input parameters validation failed')
                ctx.my_output.default(reason)
                raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(images))
        bar_handler.goto(0)
        failed = []
        for item in images:
            if not image_handler.create(item):
                failed.append(item)
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some create tasks failed')
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
