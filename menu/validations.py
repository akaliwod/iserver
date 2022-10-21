import os
import traceback
import click
import yaml

from lib import iaccount_helper
from lib import ip_helper
from lib import my_servers_helper
from lib import organization
from lib import scu
from lib import os_image
from lib import hcl_operating_system
from lib import hcl_operating_system_vendor


def validate_iaccount(ctx, param, value):
    intersight_handler = iaccount_helper.IntersightAccount()
    if not intersight_handler.is_iaccount_valid(value):
        raise click.BadParameter('Invalid iaccount value')
    return value


def validate_organization(ctx, iaccount, organization_name):
    organization_handler = organization.Organization(iaccount)

    if len(organization_name) == 0:
        organizations = organization_handler.get_moids_dict()
        if len(organizations) == 0:
            ctx.busy = False
            ctx.my_output.error('No organizations found')
            return None

        if len(organizations) > 0:
            ctx.busy = False
            ctx.my_output.error('Multiple organizations found. Select single one')
            for key in organizations:
                ctx.my_output.default('- %s' % (organizations[key]))
            return None

        return list(organizations.keys())[0]

    organization_details = organization_handler.get_by_name(organization_name)
    if organization_details is None:
        ctx.busy = False
        ctx.my_output.error('Organization not found: %s' % (organization_name))
        return None

    return organization_details['Moid']


def validate_ip(ctx, param, value):
    if len(value) > 0:
        if not ip_helper.is_valid_ipv4_address(value):
            raise click.BadParameter('Invalid IPv4 address: %s' % (value))
    return value


def validate_prefix_length(ctx, param, value):
    if value <= 0 or value >= 30:
        raise click.BadParameter('Invalid prefix length')
    return value


def validate_yaml_file(ctx, filename):
    if not os.path.isfile(filename):
        ctx.my_output.error('File %s not found' % (filename))
        return None

    try:
        with open(filename, 'rb') as file_handler:
            content = yaml.safe_load(file_handler)

    except BaseException:
        ctx.my_output.error('YAML format required')
        ctx.my_output.traceback(traceback.format_exc())
        return None

    return content


def validate_int_oper(ctx, param, value):
    if len(value) == 0:
        return value

    for prefix in ['ge', '>=', 'le', '<=', 'gt', '>', 'lt', '<', 'ne', '!=']:
        if value.startswith(prefix):
            try:
                int_value = int(value.lstrip(prefix))
                return value
            except BaseException:
                pass
            raise click.BadParameter('Wrong value: %s' % (value))

    try:
        int_value = int(value)
        return value
    except BaseException:
        pass

    raise click.BadParameter('Wrong value: %s' % (value))


def validate_group(ctx, param, value):
    my_servers_handler = my_servers_helper.MyServers()
    if not my_servers_handler.is_group(value):
        raise click.BadParameter('Group not found: %s' % (value))
    return value


def validate_group_serials(ctx, param, value):
    if len(value) == 0:
        return []

    my_servers_handler = my_servers_helper.MyServers()
    if not my_servers_handler.is_group(value):
        raise click.BadParameter('Group not found: %s' % (value))

    serials = my_servers_handler.get_group_serials(value)
    if serials is None or len(serials) == 0:
        raise click.BadParameter('No group members found: %s' % (value))

    return serials


def validate_group_oper(ctx, param, value):
    my_servers_handler = my_servers_helper.MyServers()
    if len(value) == 0:
        return None

    group_oper = {}
    if value.startswith('+'):
        group_oper['oper'] = 'add'
        group_oper['group'] = value.lstrip('+')

    if value.startswith('-'):
        group_oper['oper'] = 'del'
        group_oper['group'] = value.lstrip('-')

    if not value.startswith('-') and not value.startswith('+'):
        group_oper['oper'] = 'set'
        group_oper['group'] = value
        return group_oper

    if not my_servers_handler.is_group(group_oper['group']):
        raise click.BadParameter('Group not found: %s' % (value))

    return group_oper


def validate_filter_serials(ctx, param, value):
    if len(value) == 0:
        return []
    return value.split(',')


def validate_filter_ip(ctx, param, value):
    if len(value) == 0:
        return []

    ip_filter = []
    for item in value.split(','):
        if ip_helper.is_valid_ipv4_address(item):
            ip_filter.append(
                dict(
                    type='address',
                    value=item
                )
            )
            continue

        if ip_helper.is_valid_ipv4_cidr(item):
            ip_filter.append(
                dict(
                    type='subnet',
                    value=item
                )
            )
            continue

        raise click.BadParameter('Invalid IP address or subnet value: %s' % (item))

    return ip_filter


def validate_scu(ctx, iaccount, scu_name, required=True):
    if len(scu_name) == 0:
        if required:
            ctx.my_output.error('SCU value required')
            return None
        return scu_name

    scu_handler = scu.SoftwareConfigurationUtility(iaccount)
    scu_item = scu_handler.get_by_name(scu_name)
    if scu_item is None:
        ctx.my_output.error('SCU not found: %s' % (scu_name))
        return None

    return scu_item


def validate_os_image(ctx, iaccount, image_name, required=True):
    if len(image_name) == 0:
        if required:
            ctx.my_output.error('OS image value required')
            return None
        return image_name

    image_handler = os_image.OsImage(iaccount)
    image_item = image_handler.get_by_name(image_name)
    if image_item is None:
        ctx.my_output.error('Image not found: %s' % (image_name))
        return None

    vendor_handler = hcl_operating_system_vendor.HclOperatingSystemVendor(iaccount)
    vendor_item = vendor_handler.get_by_name(image_item['Vendor'])
    if vendor_item is None:
        ctx.my_output.error('Image vendor not found: %s' % (image_item['Vendor']))
        return None
    image_item['VendorId'] = vendor_item['Moid']

    version_handler = hcl_operating_system.HclOperatingSystem(iaccount)
    version_item = version_handler.get_vendor_version(vendor_item['Moid'], image_item['Version'])
    if version_item is None:
        ctx.my_output.error('Image version not found: %s' % (image_item['Version']))
        return None

    image_item['VersionId'] = version_item['Moid']

    return image_item
