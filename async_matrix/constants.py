from pathlib import Path

BASEDIR = Path(__file__).resolve().parent
PANEL_WIDTH = 1200
PANEL_HIGHLY = 1000
FONT_PX = 60
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
TEXT_VECTOR = tuple((0.5, -0.25))
HOST = "http://0.0.0.0:8080/"
