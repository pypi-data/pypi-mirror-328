import httpx


class URLSchemaMissingError(ValueError):
    def __init__(self, url: str):
        super().__init__(f'Url {url} is missing a schema')


class LMSConnectionError(ConnectionError):
    def __init__(self, response: httpx.Response):
        msg = f"Connection to {response.request.url} was refused with response '{response.status_code} - {response.text}'"
        super().__init__(msg)


class PlayerNotFoundError(ValueError):
    def __init__(self, **kwargs):
        try:
            key, value = next(iter(kwargs.items()))
            msg = f'Player with {key} "{value}" not found'
        except StopIteration:
            msg = 'Player not found'

        super().__init__(msg)


class SecondsInputError(ValueError):
    def __init__(self, seconds: float) -> None:
        super().__init__(f'Number of seconds ({seconds}) not positive')


class VolumeInputError(ValueError):
    def __init__(self, volume) -> None:
        super().__init__(f'New volume must be between 0 and 100 not {volume}')
