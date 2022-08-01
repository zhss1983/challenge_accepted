import aiohttp
import asyncio
from aiohttp.client_exceptions import ClientError, ClientConnectorError

from divide import Divider, Divisible
from utils import get_numbers
from constants import EXIT_KEY, MAX_DECIMAL_PLACES, HOST
from logger import logger


class Divider5(Divider):
    @property
    def is_devision(self):
        """Проверяет делимость на 5"""
        return self.numbers[-1] in (0, 5)


class Divider3(Divider):
    @property
    def is_devision(self):
        """
        Проверяет делимость на 3.
        Проверка формальная, не оптимальная, но математически верная.
        А почему бы и нет, ведь весь код всего лиш шутка юмора.
        """
        sum_numbers = sum(self.numbers)
        while sum_numbers > 9:
            numbers = (int(number) for number in str(sum_numbers))
            sum_numbers = sum(numbers)

        return sum_numbers % 3 == 0


async def run():
    print("Для выхода нажмите: q.")
    divisible = Divisible(MAX_DECIMAL_PLACES)
    div_on_3 = Divider3(divisible, ["foo", "FOO", "Foo"])
    div_on_5 = Divider5(divisible, ["bar", "BAR", "Bar"])

    numbers = get_numbers(EXIT_KEY)

    for num in numbers:
        if not isinstance(num, int):
            if num == "\n":
                divisible.clear()
            continue
        divisible.add(num)
        msg = div_on_3.message if div_on_3.is_devision else ""
        msg += div_on_5.message if div_on_5.is_devision else ""
        if msg:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(HOST + msg) as response:
                        answer = await response.text()
                        if answer != msg:
                            raise ClientError
            except ClientConnectorError:
                logger.exception("Нет связи с сервером (%s).", HOST)
            except ClientError:
                logger.exception("Сервер (%s) ответил не корректно.", HOST)
            number = "".join(map(str, divisible.numbers))
            logger.info("Введено число %s, отправлено сообщение %s", number, msg)
        await asyncio.sleep(0.001)


if __name__ == "__main__":
    asyncio.run(run())
