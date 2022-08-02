import random

import aiohttp
import asyncio
from aiohttp.client_exceptions import ClientError, ClientConnectorError

from divide import Divider, Divisible
from constants import MAX_DECIMAL_PLACES, HOST
from logger import logger

MESSAGE_COUNT = 10000  # 100
DELAY = 0.001  # 1


async def run():
    divisible = Divisible(MAX_DECIMAL_PLACES)
    div_on_3 = Divider(divisible, ["foo", "FOO", "Foo"])
    div_on_5 = Divider(divisible, ["bar", "BAR", "Bar"])

    logger.info("Запущен цикл тестовой отправки сообщений. Логируются только ошибки.")
    for count in range(MESSAGE_COUNT):
        msg = div_on_3.message if random.random() > 0.5 else ""
        msg += div_on_5.message if random.random() > 0.5 else ""
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
        await asyncio.sleep(DELAY)


if __name__ == "__main__":
    asyncio.run(run())
