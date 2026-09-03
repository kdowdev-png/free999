import discord
from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

        async def on_ready(self):
            print(f'Logged in as {self.user.name} ({self.user.id})')

            async def setup(self):
                await self.add_cog(SetupCog(self))
                await self.add_cog(VoiceCog(self))

                class SetupCog(commands.Cog):
                    def __init__(self, bot):
                        self.bot = bot

                        @commands.command(name='setname', help='Change the bot's name" )
    async def set_name(self, ctx, *, name: str):
        try:
            await self.bot.user.edit(username=name)
            await ctx.send(__PYSTR_1__)
        except discord.HTTPException as e:
            await ctx.send(__PYSTR_2__)

    @commands.command(name='setavatar', help='Change the bot's profile picture')
                        async def set_avatar(self, ctx, url: str):
                            try:
                                async with aiohttp.ClientSession() as session:
                                    async with session.get(url) as resp:
                                        if resp.status != 200:
                                            await ctx.send('Could not download image.')
                                            return
                                            data = await resp.read()
                                            await self.bot.user.edit(avatar=data)
                                            await ctx.send('Bot profile picture changed.')
                                            except discord.HTTPException as e:
                                                await ctx.send(f'Failed to change bot profile picture: {e}')

                                                @commands.command(name='status', help='Display the bot's current status')
    async def status(self, ctx):
        await ctx.send(__PYSTR_4__)

class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='Join a voice channel')
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()
        await ctx.send(__PYSTR_5__)

    @commands.command(name='leave', help='Leave the voice channel')
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
            await ctx.send('Left the voice channel')
        else:
            await ctx.send('Not in a voice channel')

intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(command_prefix='!', intents=intents)

async def main():
    await bot.setup()
    await bot.start('MTQ2MDY2MjM2OTc2MzE5NzAzOQ.GozEa9._ULXm6roSFuNKteeTWd8cS0UzwhTBOHHWshzd')

if __name__ == '__main__':
                                                import asyncio
                                                asyncio.run(main())
