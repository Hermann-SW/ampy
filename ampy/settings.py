from pathlib import Path
from tempfile import gettempdir

from decouple import config
from esptool import ESPLoader

BAUD = config("AMPY_BAUD", ESPLoader.ESP_ROM_BAUD, cast=int)
TMP_DIR = Path(gettempdir()) / "ampy"
CACHE_DIR = Path.home() / ".cache" / "ampy"

MPY_REPO_URL = "https://github.com/micropython/micropython.git"
MPY_REPO_DIR = CACHE_DIR / "micropython"


for dir in TMP_DIR, CACHE_DIR:
    try:
        dir.mkdir()
    except FileExistsError:
        pass
