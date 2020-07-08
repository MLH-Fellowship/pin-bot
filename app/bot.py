import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='/')

def main():
    load_dotenv()    
    bot.run(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print("Ready!")
    activity = discord.Activity(name="for pinned messages",
                                      type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(description="Pin a message. Argument: URL of message to be pinned")
async def pin(ctx):
    message = await get_message(ctx)
    try:
        await message.pin()
    except:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")

@bot.command(description="Unpin a message. Argument: URL of message to be unpinned")
async def unpin(ctx):
    message = await get_message(ctx)
    try:
        await message.unpin()
        await ctx.send("Unpinned!")
    except:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")

async def get_message(ctx):
    message_url = ctx.message.clean_content.split(' ')[1]

    # Check if url is from Discord
    if message_url[:23] == "https://discordapp.com/":
        try:
            id = message_url[-18:]
            return await ctx.message.channel.fetch_message(id)
        except:
            return None
    else:
        return None        

if __name__ == '__main__':
    main()
