from matrix import run, drops, drop_init, chars_green

import asyncio
from aiohttp import web


async def handle(request):
    text = request.match_info.get("message", "")
    drops.append(drop_init(chars_green, text))
    return web.Response(text=text)


async def server():
    app = web.Application()
    app.add_routes([web.get("/{message}", handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    await run()


if __name__ == "__main__":
    asyncio.run(server())
