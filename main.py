from dotenv import load_dotenv
import os
import discord
from image_download import get_new_quote
import time
from datetime import date

today = date.today()
day = today.strftime("%d/%m/%Y")

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_message(message):
	if message.content == "!quote":
		title = "Daily quote for " + str(day)
		await message.channel.send(title)
		await message.channel.send(file=discord.File('quote.png'))
		await message.delete()
		get_new_quote()
		
bot.run(TOKEN)