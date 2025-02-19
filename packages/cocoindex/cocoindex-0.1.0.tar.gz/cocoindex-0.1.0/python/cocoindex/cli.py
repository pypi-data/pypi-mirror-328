import click

from . import flow
from .setup import check_setup_status, CheckSetupStatusOptions, apply_setup_changes

@click.group()
def cli():
    """
    CLI for Cocoindex.
    """

@cli.command()
def ls():
    """
    List all available flows.
    """
    for name in flow.flow_names():
        click.echo(name)

@cli.command()
@click.option("--name", type=str, required=False)
def show(name: str | None):
    """
    Show the flow spec.
    """
    click.echo(str(_flow_by_name(name)))

@cli.command()
@click.option(
    "-D", "--delete_legacy_flows", is_flag=True, show_default=True, default=False,
    help="Also check / delete flows existing before but no longer exist.")
def setup(delete_legacy_flows):
    """
    Check and apply setup changes.
    """
    options = CheckSetupStatusOptions(delete_legacy_flows=delete_legacy_flows)
    status_check = check_setup_status(options)
    print(status_check)
    if status_check.is_up_to_date():
        return
    if not click.confirm(
        "Changes need to be pushed. Continue? [yes/N]", default=False, show_default=False):
        return
    apply_setup_changes(status_check)

def _flow_name(name: str | None) -> str:
    names = flow.flow_names()
    if name is not None:
        if name not in names:
            raise click.BadParameter(f"Flow {name} not found")
        return name
    if len(names) == 0:
        raise click.UsageError("No flows available")
    elif len(names) == 1:
        return names[0]
    else:
        raise click.UsageError("Multiple flows available, please specify --name")

def _flow_by_name(name: str | None) -> flow.Flow:
    return flow.flow_by_name(_flow_name(name))
