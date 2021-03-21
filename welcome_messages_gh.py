import discord
import datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


IDSERVER = ''
IDCHANNEL = ''
INVITELINK = ''

async def onReadyAction(myClient):
    print('The bot is ready.')
    return await myClient.change_presence(activity=discord.Streaming(name="evodka", url='https://www.twitch.tv/ev0dka'))


@client.event
async def on_ready():
    return await onReadyAction(client)


async def onMemberJoinAction(myClient, myMember):
    print('here')
    guild = myClient.get_guild(IDSERVER)
    channel = guild.get_channel(IDCHANNEL)
    await channel.send(f'Welcome to the server {myMember.mention}! :crown:') #welcome the member to the server
    await myMember.send(f'Welcome to {guild.name} server, {myMember.name}!')  # welcome thru dms
    embed = discord.Embed(title=f"{myMember.name} just joined!", colour=(0xff001f),
                          description=f"Welcome to [{guild.name}]({INVITELINK}) server! You are the {len(list(myMember.guild.members))} member! ```\nHave fun!```")
    embed.set_thumbnail(url=f"{myMember.avatar_url}")
    embed.set_author(name=f"{myMember.name}", icon_url=f"{myMember.avatar_url}")
    embed.set_footer(text="evodka", icon_url=f"{myMember.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    return await onMemberJoinAction(client, member)


async def onMemberRemoveAction(myClient, myMember):
    guild = myClient.get_guild(IDSERVER)
    channel = guild.get_channel(IDCHANNEL)
    await channel.send(f'{myMember.mention} left the server')


@client.event
async def on_member_remove(member):
    return await onMemberRemoveAction(client, member)


client.run('TOKEN')
