import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

def main():
    load_dotenv()    
    bot.run(os.getenv("TOKEN"))

@bot.command(description="Pin a message")
async def pin(ctx):
    message = await get_message(ctx)
    await message.pin()
    await ctx.send("Pinned!")

@bot.command(description="Unpin a message")
async def unpin(ctx):
    message = await get_message(ctx)
    await message.unpin()
    await ctx.send("Unpinned!")

async def get_message(ctx):
    message_url = ctx.message.clean_content.split(' ')[1]

    # Check if url is from Discord
    if message_url[:23] == "https://discordapp.com/":
        print(message_url)
        id = message_url[-18:]
        return await ctx.message.channel.fetch_message(id)

    else:
        await ctx.send("Invalid URL")
        return None        
