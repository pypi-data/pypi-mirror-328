# lms-control

[![PyPI - Version](https://img.shields.io/pypi/v/lms-control.svg)](https://pypi.org/project/lms-control)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lms-control.svg)](https://pypi.org/project/lms-control)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
$ pip install lms-control
```

## Usage

The command line tool can be used to control players connected to a [lyrion media server](https://lyrion.org/).

```console
$ lms --help
Usage: lms [OPTIONS] COMMAND [ARGS]...

  Simple command line tool to control lyrion media server players.

Options:
  --help  Show this message and exit.

Commands:
  mute         Mutes the volume
  next         Starts the playback of the next song
  pause        Pauses the playback
  play         Starts the playback
  players      List the available players
  previous     Starts the playback of the previous song
  stop         Stops the current playback
  volume_down  Decrease the playback volume
  volume_up    Increase the playback volume
```

## License

`lms-control` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
