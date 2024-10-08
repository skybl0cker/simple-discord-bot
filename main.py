import discord
import asyncio
from discord.ext import commands
from datetime import datetime
import pytz

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

est = pytz.timezone('America/New_York')

CHANNEL_ID = 000000000000000000  

@client.command()
async def test(ctx):
    user = await client.fetch_user(819031405668990977)  
    await ctx.send(f"{user.mention}, the bot is working!")

async def send_message_at_time():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        now = datetime.now(est)
        if (now.hour == 14 and now.minute == 54) or (now.hour == 23 and now.minute == 11):
            current_time = now.strftime("%I:%M %p %Z") 
            await channel.send(f"It's {current_time} right now!")
            await asyncio.sleep(60)  
        else:
            await asyncio.sleep(30) 

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    user = await client.fetch_user(000000000000) 
    await channel.send(f"{user.mention}, the bot is working!")


async def main():
    asyncio.create_task(send_message_at_time())
    await client.start('bot_token')  # Replace with your bot token

asyncio.run(main())
