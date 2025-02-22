from operator import attrgetter

import click

from lms_control.player import Player
from lms_control.server import MediaServer
from lms_control import exc

server_option = click.option(
    '-s',
    '--server',
    'url',
    prompt=True,
    type=str,
    help='Lyrion Media Server interface address',
)
player_name_option = click.option(
    '-p', '--player', 'player_name', type=str, default=None, help='Player name'
)


def _get_server(url: str) -> MediaServer:
    try:
        server = MediaServer(url=url)
    except exc.URLSchemaMissingError as err:
        raise click.UsageError(
            message=f"The url '{url}' is missing a protocol. Probably 'http://...'"
        ) from err
    except exc.LMSConnectionError as err:
        raise click.UsageError(message=err.args[0]) from err
    else:
        return server


@click.group()
def cli():
    """Simple command line tool to control lyrion media server players."""
    pass


@cli.command(help='List the available players')
@server_option
def players(url: str) -> None:
    """This command provides an overview of awailable players that are currently connected to the lyrion media server"""
    server = _get_server(url=url)
    player_count = len(server.players)

    if player_count == 0:
        click.echo('No player found')
        return None

    click.echo(f'Found {player_count} players:')
    for player in server.players:
        click.echo(f' - {player.name} ({player.model_name} @{player.ip})')


def _select_player(player_name: str | None, server: MediaServer) -> Player:
    if player_name is None:
        player_name = click.prompt(
            'Select a player',
            type=click.Choice(choices=[player.name for player in server.players]),
            show_choices=True,
        )

    try:
        player = server.get_player_by_name(player_name)
    except exc.PlayerNotFoundError as e:
        msg = f'Player {player_name} not found'
        raise click.UsageError(msg) from e
    else:
        return player


for command, help in (
    ('play', 'Starts the playback'),
    ('previous', 'Starts the playback of the previous song'),
    ('next', 'Starts the playback of the next song'),
    ('stop', 'Stops the current playback'),
    ('pause', 'Pauses the playback'),
    ('mute', 'Mutes the volume'),
    ('volume_up', 'Increase the playback volume'),
    ('volume_down', 'Decrease the playback volume'),
):

    def _fct(url: str, player_name: str | None, command: str = command):
        server = _get_server(url=url)
        player = _select_player(player_name=player_name, server=server)
        attrgetter(command)(player)()

    cli.command(name=command, help=help)(server_option(player_name_option(_fct)))
