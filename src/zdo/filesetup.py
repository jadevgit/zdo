from pathlib import Path
from importlib.resources import files

CONFIG_DIR = Path.home() / ".config" / "zdo"
PROJ_DIR = p.home() / ".local" / "share" / "zdo"


def ensure_dirs() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok = True)
    PROJ_DIR.mkdir(parents=True, exist_ok = True)

    CONFIG_FILE = CONFIG_DIR / "config.toml"
    if not CONFIG_FILE.exists():
        default = files(__package__).joinpath("default_config.toml").read_text(encoding="utf-8")
        CONFIG_FILE.write_text(default, encoding="utf-8")

