import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_local_apple_image_path():
    # Ruta de la carpeta con imágenes
    folder_path = "./manzanas"
    # Lista de archivos en la carpeta
    manzanas = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    # Seleccionar una imagen aleatoria
    return random.choice(manzanas)

@bot.command('apple')
async def apple(ctx):
    '''El comando apple devuelve una foto de una manzana'''
    image_path = get_local_apple_image_path()
    # Enviar la imagen al canal
    await ctx.send(file=discord.File(image_path))


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")


bot.run('MTMxNTg0ODMyNzAyMzE2OTU3Ng.GmmxAZ.mA_Vcy5eV056CheAYhUEc-PO2Vfz2xsyHCVxTc')