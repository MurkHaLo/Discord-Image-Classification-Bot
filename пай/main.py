import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'I {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(f'Сохранили картинку в ./{attachment.filename}')
    else:
        await ctx.send('Вы забыли загрузить картинку')
bot.run('MTEyNzUzNzg5MTQ2MDAxMDA2NA.G6PHXM.2RsN_B-jVuTgSz6WyC8EvFqwgwM8PTvaLMRvGA')
