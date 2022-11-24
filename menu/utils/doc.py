import sys
import click

from lib import self_doc


@click.command("doc")
@click.pass_obj
@click.option("--directory", is_flag=False, show_default=False, default="results")
@click.option("--no-redfish", is_flag=True, show_default=True, default=False, help="Disable redfish tests")
def utils_doc_command(ctx, directory, no_redfish):
    """Generate documentation"""

    # iserver utils doc

    success = self_doc.generate_docs(
        directory,
        redfish_tests=not no_redfish
    )

    if not success:
        sys.exit(1)
