import discord
import random
import time
from discord.ext import commands
from blab import get_class
from token_1 import token

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send (f'Merhaba {bot.user}!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def sohbet(ctx):
    await ctx.send(f'Ne hakkında konuşalım?')

@bot.command()
async def gundem(ctx):
    await ctx.send(f'Bugün türkiye gündeminde yasaklanan uygulamalar var.Yasaklanan uygulamaları görmek için yasak komudunu kullanın!')

@bot.command()
async def yasak(ctx):
    await ctx.send(f'Roblox')
    time.sleep(1)
    await ctx.send(f'spor haberleri için spor komudunu kullanın!')

@bot.command()
async def spor(ctx):
    await ctx.send(f'dünki Fenerbahçe-Lille maçı 1-1  sonuçlandı')
    time.sleep(1)
    await ctx.send(f'şu anki işlevim bu kadar dahası için geliştiriliyorum sonra görüşmek üzere!')

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        await ctx.send("Resim/ler algılandı!")
        await ctx.send("Sınıflandırma başladı!")
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f'images/{file_name}'
            await attachment.save(file_path)
            await ctx.send("Resim kaydedildi!")
            name, score = get_class(file_path ,"keras_model.h5" , "labels.txt")
            await ctx.send(f"resimde {name} olduğunu düşünüyorum.Ve bundan %{score*100} eminim")
    else:
        await ctx.send("Resim algılanmadı! Lütfen bir resim ekleyin!")



bot.run(token)