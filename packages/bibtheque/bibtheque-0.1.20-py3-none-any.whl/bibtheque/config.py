import tomllib
from pathlib import Path

#  ──────────────────────────────────────────────────────────────────────────

# default configuration
config = {'index': {'path': '~/.bibtheque/index.json'},
          'database': {'host': '0.0.0.0',
                       'host_port': 2340,
                       'path': '~/.bibtheque_db/',
                       'cache': '~/.cache/bibtheque',
                       'cache_port': 2340,
                       },
          }

# default config path
config_path = Path("~/.config/bibtheque.toml").expanduser()

if config_path.exists():
    with open(config_path, 'rb') as file:
        tmp = tomllib.load(file)

    # set configuration from toml
    for key in tmp.keys():
        config[key] = tmp[key]
