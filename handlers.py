import tornado.web
import config, services


class DiscordLogsHandler(tornado.web.RequestHandler):
    _channels = {
        'server': config.DISCORD_SERVER_LOGS_ID,
        'backup': config.DISCORD_BACKUP_LOGS_ID,
    }

    async def post(self, channel_key):
        if channel_key not in self._channels:
            raise Exception('Invalid channel name')

        channel = services.bot.get_channel(self._channels[channel_key])

        if self.request.body:
            await channel.send(self.request.body.decode('utf-8'))
