from pathlib import Path
from typing import Dict

current = Path(__file__).parent.absolute()
resources = current.parent.joinpath('assets').absolute()

cesty: Dict[str, Path] = {
    'assets': current.parent.joinpath('assets').absolute(),
    'player': current.parent.joinpath('assets/textures/player').absolute(),
    'terrain': current.parent.joinpath('assets/textures/terrain').absolute(),
    'tmx': current.parent.joinpath('assets/maps/tmx').absolute(),
}