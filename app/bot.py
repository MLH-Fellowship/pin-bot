import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv


reaction_emoji = '📌'

prefix_map = {
    reaction_emoji: ''
}


def select_command_prefix(_bot, message):
    return prefix_map.get(message.clean_content[0], '/')


bot = commands.Bot(command_prefix=select_command_prefix,
                   description=f"You can now react to messages with {reaction_emoji} to pin a message!")


@bot.event
async def on_ready():
    print("Ready!")
    activity = discord.Activity(name="/help pin to get started!",
                                type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.event
async def on_raw_reaction_add(payload):
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if payload.emoji.name == reaction_emoji:
        if not message.pinned:
            await message.pin()
        else:
            pin_reaction = {
                r.emoji: r for r in message.reactions
            }.get(reaction_emoji)

            if pin_reaction and pin_reaction.me:
                await message.remove_reaction(reaction_emoji, bot.user)


@bot.event
async def on_raw_reaction_remove(payload):
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if payload.emoji.name == reaction_emoji and message.pinned:
        await message.unpin()
        await message.clear_reaction(reaction_emoji)
        await channel.send("Unpinned!")


@bot.command(description="Pin a message. Argument: URL of the  message to be pinned or message itself", aliases=[reaction_emoji])
async def pin(ctx):
    try:
        message = await get_message_from_url(ctx)
        if not message:
            message = ctx.message

        if message.pinned == True:
            await ctx.send("Message is already pinned")
        else:
            # this will trigger on_raw_reaction_add to actually pin the message
            await message.add_reaction(reaction_emoji)
    except Exception:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")


@bot.command(description="Unpin a message. Argument: URL of message to be unpinned")
async def unpin(ctx):
    message = await get_message_from_url(ctx)

    try:
        if message.pinned == False:
            await ctx.send("Message is not pinned")
        else:
            # this will trigger on_raw_reaction_remove to actually unpin the message
            await message.remove_reaction(reaction_emoji, bot.user)
    except Exception:
        await ctx.send("Something went wrong. Make sure your URL is correct and valid.")


async def get_message_from_url(ctx):
    message_url = ctx.message.clean_content.split(' ')[1]

    # Check if url is from Discord
    if message_url[:23] == "https://discordapp.com/" or message_url[:20] == "https://discord.com/":
        try:
            ids = message_url.split('/')
            if len(ids) == 7:
                return await ctx.message.channel.fetch_message(ids[-1])
            else:
                return None
        except Exception:
            return None
    else:
        return None


def main():
    load_dotenv()
    sys.stdout.flush()
    bot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    main()
