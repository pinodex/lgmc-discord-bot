import discord


class DiscordWrapper(discord.Client):
    def __init__(self, loop, guild_id):
        self.guild_id = int(guild_id)

        super().__init__(loop=loop)

    async def on_ready(self):
        print('Logged on as', self.user)

        self.guild = self.get_guild(self.guild_id)
        print('Connected to guild "%s"' % self.guild.name)
