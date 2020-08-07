import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='!')


#start up confirmation
@client.event

async def on_ready():

    print('We have logged in as {0.user}'.format(client))


client.remove_command('help')


@client.command()
async def help(ctx):
    """""
    !help command
    must be updated with new commands
    """
    await ctx.send('Current list of commands:\n\n!uwu : forbidden command, don\'t use it >:( \n!weeb_hunt : requires user mention following command eg. \'!weeb_hunt @user\'\n!help_trial : you\'re already here!')

@client.command()
async def uwu(ctx):
    """
    pretends to 'insta-ban' user
    """
    await ctx.send(ctx.author.mention + ' has been insta banned')

@client.command()
async def weeb_hunt(ctx,user:discord.User):
    """
    user can call out another as a 'weeb', part of secret weeb game (upcoming)

    """
    response = "{} has accused {} of being a weeb!"
    choice= response
    choice = choice.format(ctx.author.mention, user.mention)
    await ctx.send(choice)
#@client.event
#async def on_message(message):
#    if message.content.startswith('!weeb_hunt'):

#        user=message.mentions[0]
#        response = "{} has accused {} of being a weeb!"
#        choice= response
#        choice = choice.format(message.author.mention, user.mention)
#        await message.channel.send(choice)


    #role=get(member.server.roles,name="test")
    #await bot.add_roles(member,role)

    #if message.content.startswith('!flex'):
     #   user = discord.utils.get(message.server.members
      #  await message.channel.send()



client.run('NzM5MjYxMTg3OTg3OTk2ODQz.XyX4og.y-Py2K_Ote0ky9A1Yy29Fg-CGqE')