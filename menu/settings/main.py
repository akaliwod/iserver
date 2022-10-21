import sys
import json
import click

from lib import iaccount_helper
from lib import settings_helper
from lib import my_servers_helper
from lib import my_server_helper
from menu import validations
from menu import defaults


@click.group("settings")
@click.pass_obj
def settings_menu(ctx):
    """Settings"""


@settings_menu.group("defaults")
@click.pass_obj
def settings_defaults_menu(ctx):
    """Defaults"""


@settings_defaults_menu.command("get")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def settings_defaults_get_command(ctx, output):
    """Show Default Settings"""

    # iwectl settings defaults get

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()
    if values is None:
        ctx.my_output.error('Get settings failed')
        sys.exit(1)

    if output == 'json':
        ctx.my_output.default(json.dumps(values, indent=4))
        return

    ctx.my_output.dictionary(
        values,
        exclude=[],
        title='Default Settings',
        underline=True,
        prefix='- ',
        justify=True
    )


@settings_defaults_menu.command("rfd")
@click.pass_obj
def settings_defaults_rfd_command(ctx):
    """Revert default settings to factory defaults"""

    # iwectl settings defaults rfd

    settings_handler = settings_helper.Settings()
    if not settings_handler.rfd_settings():
        ctx.my_output.error('Set settings failed')
        sys.exit(1)

    ctx.my_output.default('Done')


@settings_menu.group("repository")
@click.pass_obj
def settings_repository_menu(ctx):
    """External repository"""


@settings_repository_menu.command("get")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def settings_repository_get_command(ctx, output):
    """Show defined repositories"""

    # iwectl settings repository get

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()

    if output == 'json':
        ctx.my_output.default(json.dumps(values['repository'], indent=4))
        return

    if len(values['repository']) == 0:
        ctx.my_output.default('No repository entries defined')
        return

    ctx.my_output.my_table(
        values['repository'],
        order=[
            'name',
            'url'
        ],
        headers=[
            'Name',
            'URL'
        ],
        table=True
    )


@settings_repository_menu.command("add")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
@click.argument("url", required=True, type=click.STRING)
def settings_repository_add_command(ctx, name, url):
    """Add repository setting"""

    # iwectl settings repository add

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()

    for repository in values['repository']:
        if repository['name'] == name:
            ctx.my_output.error('Repository %s is already defined' % (name))
            sys.exit(1)

    values['repository'].append(
        dict(
            name=name,
            url=url
        )
    )

    if not settings_handler.set_settings(values):
        ctx.my_output.error('Settings save failed')
        sys.exit(1)

    ctx.my_output.default('Settings saved')


@settings_repository_menu.command("delete")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
def settings_repository_delete_command(ctx, name):
    """Delete repository setting"""

    # iwectl settings repository delete

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()

    repository_entries = []
    for repository in values['repository']:
        if repository['name'] != name:
            repository_entries.append(repository)

    values['repository'] = repository_entries
    if not settings_handler.set_settings(values):
        ctx.my_output.error('Settings save failed')
        sys.exit(1)

    ctx.my_output.default('Settings saved')


@settings_repository_menu.command("clear")
@click.pass_obj
def settings_repository_clear_command(ctx):
    """Clear repository settings"""

    # iwectl settings repository clear

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()
    values['repository'] = []
    if not settings_handler.set_settings(values):
        ctx.my_output.error('Settings save failed')
        sys.exit(1)

    ctx.my_output.default('Settings saved')


@settings_menu.group("my-servers")
@click.pass_obj
def settings_my_servers_menu(ctx):
    """My Servers"""


@settings_my_servers_menu.command("get")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def settings_my_servers_get_command(ctx, output):
    """Show my servers"""

    # iwectl settings my-servers get

    my_servers = my_servers_helper.MyClusters()
    servers = my_servers.get_my_servers()
    if servers is None:
        ctx.my_output.error('My servers not found')
        sys.exit(1)
    if len(servers) == 0:
        ctx.my_output.default('My servers not defined')
        return

    if output == 'json':
        ctx.my_output.default(json.dumps(servers, indent=4))
    else:
        ctx.my_output.my_table(
            servers,
            order=['iaccount'],
            headers=['Intersight Accout']
        )


@settings_my_servers_menu.command("add")
@click.pass_obj
@click.argument("cluster-name", required=True, type=click.STRING)
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
def settings_my_servers_add_command(ctx, cluster_name, iaccount):
    """Add cluster to my clusters"""

    # iwectl settings my-clusters add

    my_clusters_handler = my_clusters_helper.MyClusters()

    if my_clusters_handler.is_my_cluster(iaccount, cluster_name):
        ctx.my_output.default('Already defined')
        return

    success, response = my_clusters_handler.add(iaccount, cluster_name)
    if not success:
        ctx.my_output.error(response)
        sys.exit(1)

    ctx.my_output.default('Added')


@settings_my_servers_menu.command("clear")
@click.pass_obj
def settings_my_servers_clear_command(ctx):
    """Clear my clusters settings"""

    # iwectl settings my-clusters clear

    my_clusters_handler = my_clusters_helper.MyClusters()
    if not my_clusters_handler.clear_my_clusters():
        ctx.my_output.error('Failed')
        sys.exit(1)

    ctx.my_output.default('Cleared')


@settings_my_servers_menu.command("delete")
@click.pass_obj
@click.argument("cluster-name", required=True, type=click.STRING)
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
def settings_my_servers_delete_command(ctx, cluster_name, iaccount):
    """Delete cluster from my clusters"""

    # iwectl settings my-clusters delete

    my_clusters_handler = my_clusters_helper.MyClusters()

    if not my_clusters_handler.is_my_cluster(iaccount, cluster_name):
        ctx.my_output.response('Already deleted')
        return

    success, response = my_clusters_handler.delete(iaccount, cluster_name)
    if not success:
        ctx.my_output.error(response)
        sys.exit(1)

    ctx.my_output.default('Deleted')


@settings_my_servers_menu.command("set-default")
@click.pass_obj
def settings_my_servers_set_default_command(ctx):
    """Set --my-clusters option default to True value"""

    # iwectl settings my-clusters set-default

    settings_handler = settings_helper.Settings()
    if not settings_handler.set_setting('my-clusters', True):
        ctx.my_output.error('Settings update failed')
        sys.exit(1)

    ctx.my_output.default('Done')


@settings_my_servers_menu.command("unset-default")
@click.pass_obj
def settings_my_servers_unset_default_command(ctx):
    """Set --my-clusters option default to False value"""

    # iwectl settings my-clusters unset-default

    settings_handler = settings_helper.Settings()
    if not settings_handler.set_setting('my-clusters', False):
        ctx.my_output.error('Settings update failed')
        sys.exit(1)

    ctx.my_output.default('Done')


@settings_menu.group("iaccount")
@click.pass_obj
def settings_iaccount_menu(ctx):
    """Intersight Account"""


@settings_iaccount_menu.command("add")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
@click.argument("isctl-yaml", required=True, type=click.STRING)
def settings_iaccount_add_command(ctx, iaccount, isctl_yaml):
    """Create Intersight Account from isctl yaml file"""

    # iwectl settings iaccount add

    iaccount_handler = iaccount_helper.IntersightAccount()

    if not iaccount_handler.verify_isctl_configuration(filename=isctl_yaml):
        ctx.my_output.error('ISCT configuration verification failed')
        sys.exit(1)

    configuration = iaccount_handler.get_isctl_configuration(filename=isctl_yaml)
    if not iaccount_handler.create_iaccount(iaccount, configuration):
        ctx.my_output.error('Intersight Account create failed')
        sys.exit(1)

    ctx.my_output.default('Added')


@settings_iaccount_menu.command("get")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--show-key", is_flag=True, show_default=True, default=False, help="Show key")
def settings_iaccount_get_command(ctx, output, show_key):
    """Show Intersight Accounts"""

    # iwectl settings iaccount get

    iaccount_handler = iaccount_helper.IntersightAccount()
    accounts = iaccount_handler.get_iaccounts()

    if not show_key:
        new_accounts = []
        for account in accounts:
            account['keyid'] = '*****'
            new_accounts.append(account)
        accounts = new_accounts

    if output == 'json':
        ctx.my_output.default(json.dumps(accounts, indent=4))
        return

    ctx.my_output.my_table(
        accounts,
        order=['name', 'keyfile', 'server', 'keyid'],
        headers=['iaccount', 'key file', 'server', 'key id'],
        table=True
    )


@settings_iaccount_menu.command("delete")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
def settings_iaccount_delete_command(ctx, iaccount):
    """Delete Intersight Account"""

    # iwectl settings iaccount delete

    iaccount_handler = iaccount_helper.IntersightAccount()
    success, reason = iaccount_handler.delete_iaccount(iaccount)
    if not success:
        ctx.my_output.error(reason)
        sys.exit(1)

    ctx.my_output.default('Deleted')


@settings_iaccount_menu.command("set-default")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
def settings_iaccount_set_default_command(ctx, iaccount):
    """Set as default Intersight Account"""

    # iwectl settings iaccount set-default

    iaccount_handler = iaccount_helper.IntersightAccount()
    if not iaccount_handler.set_default_iaccount(iaccount):
        ctx.my_output.error('Failed')
        sys.exit(1)

    ctx.my_output.default('Set as default')
