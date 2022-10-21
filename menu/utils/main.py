import sys
import json
import click

from lib import log_helper
from lib import self_doc
from lib import self_testing
from menu import defaults
from menu import validations


@click.group("utils")
@click.pass_obj
def utils_menu(ctx):
    """Extra Utils"""


@utils_menu.group("devel")
@click.pass_obj
def utils_devel_menu(ctx):
    """Development Utils"""


@utils_devel_menu.group("cli")
@click.pass_obj
def utils_devel_cli_menu(ctx):
    """iserver cli debug"""


@utils_devel_cli_menu.command("list")
@click.pass_obj
def utils_devel_cli_list_command(ctx):
    """Show last commands history"""

    # iserver utils devel cli list

    log_handler = log_helper.Log()
    log_handler.show_last_logs()


@utils_devel_cli_menu.command("bug")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
def utils_devel_cli_bug_command(ctx, name):
    """Submit bug report"""

    # iserver utils devel cli bug

    log_handler = log_helper.Log()
    log_handler.bug_report(name)


@utils_devel_menu.group("doc")
@click.pass_obj
def utils_devel_doc_menu(ctx):
    """iserver self documentation"""


@utils_devel_doc_menu.command("generate")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default="results")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose")
def utils_devel_doc_generate_command(ctx, directory, dry_run, verbose):
    """iserver generate documentation"""

    # iserver utils devel doc generate

    self_doc.generate_docs(directory, verbose, dry_run)


@utils_devel_menu.group("test")
@click.pass_obj
def utils_devel_self_test_menu(ctx):
    """iserver self tests"""


@utils_devel_self_test_menu.group("get")
@click.pass_obj
def utils_devel_self_test_get_menu(ctx):
    """get iserver tests"""


@utils_devel_self_test_get_menu.command("test-names")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_devel_self_test_get_test_names_command(ctx, directory):
    """get iserver test names"""

    # iserver utils devel self-test get test-names

    names = self_testing.get_tests(directory, names=True)
    if names is None:
        print('No tests found')
        return

    for name in names:
        print(name)


@utils_devel_self_test_get_menu.command("test-name")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_devel_self_test_get_test_name_command(ctx, name, directory):
    """get iserver test name"""

    # iserver utils devel self-test get test-name

    test = self_testing.get_test(name, directory)
    if test is None:
        print('Test not found')
        return

    print(json.dumps(test, indent=4))


@utils_devel_self_test_get_menu.command("test-collection")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_devel_self_test_get_test_collection_command(ctx, name, directory):
    """get iserver test collection info"""

    # iserver utils devel self-test get test-collection

    self_testing.get_tests_collection_info(name, directory)


@utils_devel_self_test_get_menu.command("test-collections")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_devel_self_test_get_test_collections_command(ctx, directory):
    """get iserver test collections"""

    # iserver utils devel self-test get test-collections

    tests = self_testing.get_tests_collections(directory, names=True)
    for test in tests:
        print(test)


@utils_devel_self_test_get_menu.command("summary")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
def utils_devel_self_test_get_summary_command(ctx, directory):
    """get iserver test summary"""

    # iserver utils devel self-test get summary

    self_testing.get_summary(directory, replace=True)


@utils_devel_self_test_menu.command("run")
@click.pass_obj
@click.option("--test-name", is_flag=False, show_default=False, default=None, type=click.STRING, help="Specific test selected by name")
@click.option("--test-collection", is_flag=False, show_default=False, default=None, type=click.STRING, help="Filename with test names")
@click.option("--tests", "tests_directory", is_flag=False, show_default=False, default='tests', type=click.STRING, help="Test definitions")
@click.option("--results", "results_directory", is_flag=False, show_default=False, default='results', type=click.STRING, help="Results location")
@click.option("--environment", is_flag=False, show_default=False, default='', type=click.STRING, help="Test environment")
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
def utils_devel_self_test_run_command(ctx, test_name, test_collection, tests_directory, results_directory, environment, iaccount, verbose, debug, dry_run):
    """run iserver tests"""

    # iserver utils devel self-test run

    if debug:
        verbose = True

    if test_collection is None and test_name is None:
        print('Define the scope of tests')
        sys.exit(1)

    if test_collection is not None:
        selected_tests, tests_count = self_testing.get_tests_collection(test_collection, tests_directory)
    else:
        selected_tests, tests_count = self_testing.get_test_by_name(test_name, tests_directory)

    if selected_tests is None:
        print('Test collection failed')
        sys.exit(1)

    results = self_testing.run_tests(selected_tests, tests_count, tests_directory, results_directory, environment, iaccount, verbose, debug, dry_run)
    success = 0
    for result in results:
        if result['success']:
            print("OK\t%s" % (result['command']))
            success = success + 1
        else:
            print("NOK\t%s" % (result['command']))

    print('\nSummary')
    print('- Tests: %s' % (len(results)))
    print('- Success: %s' % (success))
    print('- Failed: %s' % (len(results) - success))
