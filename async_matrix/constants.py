from dataclasses import dataclass
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int


BASEDIR = Path(__file__).resolve().parent
PANEL_WIDTH = 800
PANEL_HIGHLY = 800
FONT_PX = 40
COLUMN = int(PANEL_WIDTH / FONT_PX / 3)
LETTER = "fobar FOBAR"
# LETTER = (
#     "\n\t\"\\"
#     "1234567890"
#     "'`&^%$#@№% _~-=+*.,;:?!/|<>[]{}()"
#     "ёйцукенгшщзфывапролджэячсмитьбю"
#     "ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
#     "qwertyuiopzxcvbnm"
#     "QWERTYUIOPASDFGHJKLZXCVBNM"
# )
SPACE = ord(" ")
Q_KEY = ord("q")
MATRIX_SPEED_DALAY = 100
FONTS_COUNT = 10
TEXT_VECTOR = Point(0.5, -0.25)
HOST = "http://0.0.0.0:8080/"
