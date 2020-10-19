import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

def main():
    load_dotenv()
    sys.stdout.flush()
    bot.run(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print("Ready!")
    activity = discord.Activity(name="/pin {url} to pin a message!",
                                      type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(description="Pin a message. Argument: URL of message to be pinned")
async def pin(ctx):
    message = await get_message(ctx)
    try:
        if message.pinned == True:
            await ctx.send("Message is already pinned")
        else:
            await message.pin()
    except Exception:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")

@bot.command(description="Unpin a message. Argument: URL of message to be unpinned")
async def unpin(ctx):
    message = await get_message(ctx)
    try:
        if message.pinned == False:
            await ctx.send("Message is not pinned")
        else:
            await message.unpin()
            await ctx.send("Unpinned!")
    except:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")

async def get_message(ctx):
    message_url = ctx.message.clean_content.split(' ')[1]

    # Check if url is from Discord
    if message_url[:23] == "https://discordapp.com/" or message_url[:20] == "https://discord.com/":
        try:
            ids = message_url.split('/')
            if len(ids)  == 7: 
                return await ctx.message.channel.fetch_message(ids[-1])
            else:
                return None
        except Exception:
            return None
    else:
        return None        

if __name__ == '__main__':
    main()
