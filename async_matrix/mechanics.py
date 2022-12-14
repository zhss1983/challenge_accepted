import random
import pygame
from constants import FONT_PX, FONTS_COUNT, PANEL_HIGHLY, Point, TEXT_VECTOR


class BaseDrop:
    __wind: float = 0

    def __init__(self, *, position: Point, speed: float = 1, step: int = FONT_PX):
        self.position = position
        self.__step = step
        self.__speed = speed

    def flow(self):
        self.position.x += int(self.__step * self.__class__.__wind)
        self.position.y += int(self.__step * self.__speed)

    def __set_wind(self, wind: float):
        self.__class__.__wind = wind

    def __get_wind(self):
        return self.__class__.__wind

    wind = property(__get_wind, __set_wind, None, "Ветер для падающих объектов")


class Drop(BaseDrop):
    def __init__(self, *, chars_rendered, text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.__text = text
        self.__start_pos = -len(text) * FONT_PX
        self.__stop_pos = PANEL_HIGHLY * random.random() - self.__start_pos

        self.__chars_rendered = chars_rendered
        self.font_index = random.randint(0, FONTS_COUNT - 1)
        if text == "":
            self.font_index += 10

    def blit(self, surface: pygame.Surface):
        for shift, char in enumerate(self.__text):
            if char not in self.__chars_rendered:
                return surface
            char_img = self.__chars_rendered[char][self.font_index]
            pos_x = self.position.x + shift * FONT_PX * TEXT_VECTOR.x
            pos_y = self.position.y + shift * FONT_PX * TEXT_VECTOR.y
            surface.blit(char_img, (pos_x, pos_y))
        self.flow()

    @property
    def is_down(self):
        tail_length = len(self.__text) * FONT_PX * TEXT_VECTOR.y
        tail_out_of_windov = self.position.y + tail_length >= PANEL_HIGHLY
        had_out_of_windov = self.position.y >= PANEL_HIGHLY
        return tail_out_of_windov and had_out_of_windov
