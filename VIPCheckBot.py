import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_member_update(before, after):
    role = discord.utils.get(before.guild.roles, name='Role Name Here')
    channel = discord.utils.get(before.guild.channels, name='Channel Name Here')
    if role not in before.roles and role in after.roles:
        print(f"{before.mention} now has role.")
        await channel.send(f"{before.mention} now has role.")
    if role in before.roles and role not in after.roles:
        print(f"{before.mention} no longer has role.")
        await channel.send(f"{before.mention} no longer has role.")


@bot.slash_command(name="vibe_check", description="Determines whether or not you pass the vibe check.")
async def vibe_check(ctx):
    # Generate a random number between 1 and 2 (inclusive)
    num = random.randint(1, 2)

    # Check if the random number is 1 or 2 and display the corresponding message
    if num == 1:
        await ctx.respond("You have **failed** the vibe check.")
    else:
        await ctx.respond("You have **passed** for the vibe check.")


print('Program is running. Please minimize this window.')

bot.run("token")

