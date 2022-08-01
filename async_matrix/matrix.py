import random
import pygame
import asyncio

from constants import COLUMN, MATRIX_SPEED_DALAY
from utils import get_window_surface, get_background_surface, chars_render, drop_init, is_exit_event, random_wind

drops = []
pygame.init()
chars_green = chars_render((0, 255, 0))
chars_red = chars_render((255, 0, 0))


async def run():

    window = get_window_surface()
    background = get_background_surface()

    for _ in range(COLUMN):
        drops.append(drop_init(chars_red))

    set_wind = random_wind()

    exit_event = is_exit_event()
    while not exit_event:
        window.blit(background, (0, 0))

        for drop_index in range(COLUMN):
            drop = drops[drop_index]
            window = drop.blit(window)
            if drop.is_down or random.random() > 0.99:
                set_wind = random_wind()
                drops.pop(drop_index)
                if len(drops) < COLUMN:
                    drops.append(drop_init(chars_red))
            drop.wind = drop.wind * 0.95 + 0.05 * set_wind

        pygame.display.flip()
        exit_event = is_exit_event()
        await asyncio.sleep(MATRIX_SPEED_DALAY / 1000)
