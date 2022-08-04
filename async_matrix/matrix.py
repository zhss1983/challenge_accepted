import pygame
import asyncio

from constants import COLUMN, MATRIX_SPEED_DALAY
from utils import (
    get_window_surface,
    get_background_surface,
    chars_render,
    drop_init,
    is_exit_event,
    random_wind,
    random_dead,
)

drops = []
pygame.init()
chars_green = chars_render((0, 255, 0))
chars_red = chars_render((255, 0, 0))


async def run():

    window = get_window_surface()
    background = get_background_surface()

    for _ in range(COLUMN):
        new_drop = await drop_init(chars_red)
        drops.append(new_drop)

    set_wind = random_wind()

    while not is_exit_event():
        window.blit(background, (0, 0))
        drop_index = 0
        while drop_index < len(drops):
            drop = drops[drop_index]
            drop.blit(window)
            if drop.is_down or random_dead(drop.position.y):
                set_wind = random_wind()
                drops.pop(drop_index)
                if len(drops) < COLUMN:
                    new_drop = await drop_init(chars_red)
                    drops.append(new_drop)
            else:
                drop_index += 1
            drop.wind = drop.wind * 0.95 + 0.05 * set_wind

        pygame.display.flip()
        await asyncio.sleep(MATRIX_SPEED_DALAY / 1000)
