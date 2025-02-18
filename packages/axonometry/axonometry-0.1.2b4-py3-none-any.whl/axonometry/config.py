"""Settings class."""

# SPDX-FileCopyrightText: 2022-2025 Julien Rippinger
# SPDX-FileCopyrightText: 2019-2022 Antoine Beyeler & Contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later OR MIT

import logging
import os
import pathlib
from collections.abc import Mapping
from typing import Any

import tomli

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigManager:
    """Helper class to load axonometry's TOML configuration file.

    This class is typically used via its singleton instance ``config``::

        >>> from axonometry import config_manager
        >>> my_config = config_manager.config.get("my_config", None)

    By default, built-in configuration packaged with axonometry are loaded at startup.
    If a file exists at path ``~/.axonometry.toml``, it will be loaded as well.
    Additionaly files may be loaded using the :func:`load_config_file` method.
    """

    def __init__(self) -> None:
        self._config: dict = {}

    def load_config_file(self, path: str) -> None:
        """Load a config file and add its content to the configuration database.

        :param path: path of the config file. The configuration file must be in TOML format.
        """

        def _update(d: dict, u: Mapping) -> dict:
            """Overwrite list member, UNLESS they are list of table, in which case they must extend the list."""
            for k, v in u.items():
                if isinstance(v, dict):
                    d[k] = _update(d.get(k, {}), v)
                elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                    if k in d:
                        d[k].extend(v)
                    else:
                        d[k] = v
                else:
                    d[k] = v
            return d

        logger.info(f"loading config file at {path}")
        with open(path, "rb") as fp:
            self._config = _update(self._config, tomli.load(fp))

    @property
    def config(self) -> dict[str, Any]:
        """Access default configuration by key."""
        return self._config


config_manager = ConfigManager()


def _init() -> None:
    pathlib.Path("output/").mkdir(parents=True, exist_ok=True)
    config_manager.load_config_file(str(pathlib.Path(__file__).parent / "axo_config.toml"))
    path = os.path.expanduser("~/.aconometry.toml")
    if os.path.exists(path):
        config_manager.load_config_file(str(path))


_init()
