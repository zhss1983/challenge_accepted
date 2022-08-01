import random
import pygame

from constants import BASEDIR, FONT_PX, FONTS_COUNT, LETTER, PANEL_WIDTH, PANEL_HIGHLY, Q_KEY, SPACE
from mechanics import Point, Drop


def get_window_surface():
    surface = pygame.display.set_mode((PANEL_WIDTH, PANEL_HIGHLY))
    surface.fill((0, 0, 0))
    return surface


def get_background_surface():
    surface = pygame.Surface((PANEL_WIDTH, PANEL_HIGHLY), flags=pygame.SRCALPHA)
    surface.fill(pygame.Color(0, 0, 0, 28))
    return surface


def get_fonts():
    return tuple(
        pygame.font.Font(BASEDIR / "fonts" / f"{index}.ttf", int(FONT_PX * 0.9)) for index in range(FONTS_COUNT)
    )


def random_letter():
    return random.choice(LETTER)


def random_speed():
    return random.random() * 0.9 + 0.2


def random_start_coordinate(max_pos: int = PANEL_WIDTH - FONT_PX):
    return Point(random.randint(0, max_pos), 0)


def chars_render(color):
    fonts = get_fonts()
    chars = {char: [font.render(char, True, color) for font in fonts] for char in LETTER}
    return chars


def is_exit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            chang = pygame.key.get_pressed()
            return chang[SPACE] or chang[Q_KEY]
    return False


def drop_init(chars, text: str = ""):
    return Drop(
        chars_rendered=chars,
        text=text or random_letter(),
        position=random_start_coordinate(PANEL_WIDTH - len(text) * FONT_PX),
        speed=random_speed(),
    )


def random_wind():
    return random.random() - 0.5
