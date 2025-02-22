from __future__ import annotations

from enum import Enum, IntEnum
from typing import Any, NamedTuple

import httpx
from lms_control import exc


class Mode(Enum):
    PLAY = 'play'
    STOP = 'stop'
    PAUSE = 'pause'


class Shuffle(IntEnum):
    NO_SHUFFLE = 0
    SHUFFLE_BY_SONG = 1
    SHUFFLE_BY_ALBUM = 2


class Repeat(IntEnum):
    NO_REPEAT = 0
    REPEAT_SONG = 1
    REPEAT_PLAYLIST = 2


MAX_VOLUME = 100


class PlayerInformation(NamedTuple):
    playerindex: str
    playerid: str
    uuid: str | None
    ip: str
    name: str
    seq_no: int
    model: str
    modelname: str
    power: int
    isplaying: int
    displaytype: str
    isplayer: int
    canpoweroff: int
    connected: int
    firmware: str


class Player:
    class Playlist:
        def __init__(self, player: Player) -> None:
            self._player = player

        def clear(self):
            self._player.send_command(command='playlist clear')

        @property
        def shuffle(self) -> Shuffle:
            return Shuffle(
                int(self._player.send_command(command='playlist shuffle ?')['_shuffle'])
            )

        @shuffle.setter
        def shuffle(self, mode: Shuffle | None = None):
            self._player.send_command(command=f'playlist shuffle {mode}')

        @property
        def repeat(self) -> Repeat:
            return Repeat(
                int(self._player.send_command(command='playlist repeat ?')['_repeat'])
            )

        @repeat.setter
        def repeat(self, mode: Repeat | None = None):
            self._player.send_command(command=f'playlist repeat {mode}')

        def __getattr__(self, name):
            if name in {'name', 'url', 'modified', 'index', 'tracks'}:
                value = self._player.send_command(command=f'playlist {name} ?')[
                    f'_{name}'
                ]

                if name in {'index', 'tracks'}:
                    value = int(value)

                return value

            msg = f"{type(self._player).__name__} has not attribute 'playlist.{name}'"
            raise AttributeError(msg)

    @staticmethod
    def _send_command(
        command: str, client: httpx.Client, player_id: str | None = None
    ) -> dict[str, Any]:
        response = client.post(
            url='/jsonrpc.js',
            json={
                'id': 1,
                'method': 'slim.request',
                'params': [player_id or '', command.split(' ')],
            },
        )
        return response.json()['result']

    @classmethod
    def player_from_information(
        cls, player_information: PlayerInformation, client: httpx.Client
    ) -> Player:
        return cls(
            player_id=player_information.playerid,
            name=player_information.name,
            ip=player_information.ip,
            model_name=player_information.modelname,
            client=client,
        )

    def __init__(
        self,
        player_id: str,
        name: str,
        ip: str,
        model_name: str,
        client: httpx.Client,
    ) -> None:
        self.player_id = player_id
        self.name = name
        self.ip = ip
        self.model_name = model_name
        self._client = client
        self.playlist = self.Playlist(player=self)

    def send_command(self, command: str) -> dict[str, Any]:
        return self._send_command(
            command=command, client=self._client, player_id=self.player_id
        )

    def play(self, playlist: str | None = None, fade_in_seconds: float | None = None):
        command = 'play' if playlist is None else f'playlist play {playlist}'

        if fade_in_seconds is not None:
            command += f' {fade_in_seconds:.1f}'

        self.send_command(command=command)

    def previous(self, fade_in_seconds: float | None = None):
        command = 'playlist index -1'

        if fade_in_seconds is not None:
            command += f' {fade_in_seconds:.1f}'

        self.send_command(command=command)

    def next(self, fade_in_seconds: float | None = None):
        command = 'playlist index +1'

        if fade_in_seconds is not None:
            command += f' {fade_in_seconds:.1f}'

        self.send_command(command=command)

    def stop(self):
        self.send_command(command='stop')

    def pause(self):
        self.send_command(command='pause')

    @property
    def volume(self) -> int:
        return int(self.send_command(command='mixer volume ?')['_volume'])

    @volume.setter
    def volume(self, volume: int):
        if 0 <= volume <= MAX_VOLUME:
            self.send_command(command=f'mixer volume {volume}')
        else:
            raise exc.VolumeInputError(volume=volume)

    def volume_up(self, volume: int = 10):
        if 0 <= volume <= MAX_VOLUME:
            self.send_command(command=f'mixer volume +{volume}')
        else:
            raise exc.VolumeInputError(volume=volume)

    def volume_down(self, volume: int = 10):
        if 0 <= volume <= MAX_VOLUME:
            self.send_command(command=f'mixer volume -{volume}')
        else:
            raise exc.VolumeInputError(volume=volume)

    def mute(self):
        self.send_command(command='mixer muting')

    @property
    def mode(self) -> Mode:
        return Mode(self.send_command(command='mode ?')['_mode'])

    @property
    def time(self) -> float:
        return self.send_command(command='time ?')['_time']

    @time.setter
    def time(self, seconds: float):
        if seconds < 0:
            raise exc.SecondsInputError(seconds=seconds)

        return self.send_command(command='time {time:.2f}')

    def fast_forward(self, seconds: float):
        if seconds <= 0:
            raise exc.SecondsInputError(seconds=seconds)

        self.send_command(command=f'time +{seconds}')

    def rewind(self, seconds: float):
        if seconds <= 0:
            raise exc.SecondsInputError(seconds=seconds)

        self.send_command(command=f'time -{seconds}')

    def __getattr__(self, name):
        if name in {
            'current_title',
            'remote',
            'genre',
            'artist',
            'album',
            'title',
            'duration',
            'path',
        }:
            return self.send_command(command=f'{name} ?')[f'_{name}']

        msg = f"{type(self).__name__} has not attribute '{name}'"
        raise AttributeError(msg)

    def __repr__(self) -> str:
        return f'<Player - {self.name} ({self.player_id})>'
