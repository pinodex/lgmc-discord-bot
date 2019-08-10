import asyncio
import tornado.web
import config, services, client, handlers
from dotenv import load_dotenv


async def start_bot(loop):
    services.bot = client.DiscordWrapper(loop, config.DISCORD_GUILD_ID)
    
    await services.bot.start(config.DISCORD_BOT_TOKEN)


async def start_http(loop):
    services.http = tornado.web.Application([
        (r'/logs/(\w+)', handlers.DiscordLogsHandler),
    ], loop=loop)

    services.http.listen(config.SERVER_PORT)
    print('Server listening to port %s' % (config.SERVER_PORT,))


if __name__ == '__main__':
    load_dotenv(verbose=True)

    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(asyncio.gather(
        start_bot(loop),
        start_http(loop)
    ))
    
    loop.close()
