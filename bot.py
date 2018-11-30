
from discord.ext.commands import Bot


discordauth = "NTE1NTIzMjcxMjg2ODQ5NTM3.DuLGMg.seHG0augQfSSc3eQ-C3lRKSSpQM"
BOT_PREFIXES = ("!")
MyBot = Bot(command_prefix=BOT_PREFIXES)

@MyBot.command(aliases=["hello", "hi"], pass_context=True)
async def hello_world(context):

    response = ["Hello World!"]

    channel = context.channel
    await channel.send(response + ", " + context.message.author.mention)

MyBot.run(discordauth)
