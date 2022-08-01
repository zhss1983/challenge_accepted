import collections
import random


class Divisible:
    def __init__(self, decimal_places: int):
        self.decimal_places = decimal_places
        self.nums_deque = collections.deque(maxlen=self.decimal_places)

    def add(self, value):
        self.nums_deque.append(value)

    @property
    def numbers(self):
        return self.nums_deque

    def clear(self):
        self.__init__(self.decimal_places)


class Divider:
    def __init__(self, divisible: Divisible, messages):
        self.__divisible = divisible
        self.__msg = messages

    @property
    def is_devision(self):
        raise NotImplementedError

    @property
    def message(self):
        return random.choice(self.__msg)

    @property
    def numbers(self):
        return self.__divisible.numbers
