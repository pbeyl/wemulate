import typer
import wemulate.ext.utils as utils
import wemulate.controllers.common as common
from wemulate.core.exc import WEmulateDatabaseError, WEmulateExecutionError

app = typer.Typer(help="set parameters on a connection")


@app.command(
    help="set parameter on a specific connection, previously added parameters will be overriden",
    no_args_is_help=True,
)
def parameter(
    connection_name: str = common.CONNECTION_NAME_PARAMETER,
    delay: int = common.DELAY_PARAMETER,
    jitter: int = common.JITTER_PARAMETER,
    bandwidth: int = common.BANDWIDTH_PARAMTER,
    packet_loss: int = common.PACKET_LOSS_PARAMETER,
):
    common.check_if_connection_exists_in_db(connection_name)
    common.validate_parameter_arguments(delay, jitter, bandwidth, packet_loss)
    try:
        utils.set_parameter(
            connection_name,
            common.generate_pargs(delay, jitter, bandwidth, packet_loss),
        )
        typer.echo(f"successfully set parameters to connection {connection_name}")
    except WEmulateDatabaseError as e:
        typer.echo(e.message)
    except WEmulateExecutionError as e:
        typer.echo(e.message)
