from operator import attrgetter
from typing import Any

import urllib

import httpx

from lms_control import exc
from lms_control.player import Player, PlayerInformation


def validate_server_url(url: str) -> None:
    url_parts = urllib.parse.urlparse(url=url)
    if len(url_parts.scheme) == 0:
        raise exc.URLSchemaMissingError(url=url)


class MediaServer:
    def __init__(self, url: str):
        validate_server_url(url)
        self._client = httpx.Client(
            base_url=url,
            headers={
                'Content-Type': 'application/json',
            },
            timeout=20,
        )

        self._version = self._send_command('version ?')

    def _send_command(self, command: str) -> dict[str, Any]:
        response = self._client.post(
            url='/jsonrpc.js',
            json={
                'id': 1,
                'method': 'slim.request',
                'params': ['', command.split(' ')],
            },
        )
        if response.status_code == 200:
            return response.json()['result']

        raise exc.LMSConnectionError(response=response)

    @property
    def players(self) -> list[Player]:
        return [
            Player.player_from_information(
                player_information=PlayerInformation(**info), client=self._client
            )
            for info in self._send_command(command='players 0')['players_loop']
        ]

    def _get_player_by(self, attr: str, value: str) -> Player:
        try:
            player = next(filter(lambda x: attrgetter(attr)(x) == value, self.players))
        except StopIteration as e:
            raise exc.PlayerNotFoundError(**{attr: value}) from e
        else:
            return player

    def get_player_by_name(self, name: str) -> Player:
        return self._get_player_by(attr='name', value=name)

    def get_player_by_ip(self, ip: str) -> Player:
        return self._get_player_by(attr='ip', value=ip)

    def get_player_by_player_id(self, player_id: str) -> Player:
        return self._get_player_by(attr='player_id', value=player_id)
