import os
import sys
from io import StringIO
import discord
from discord import colour
from dotenv import load_dotenv
from discord.ext import commands
import teamverify
from teamverify.teambuilder import getTeamString, teamReasoner, teamReport, teamScore

bot = commands.Bot(command_prefix='$')
load_dotenv()
TOKEN = os.getenv('TOKEN')
POKEPASTE = 'https://pokepast.es'

def link_valid(link):
    return (len(link) == 37 or len(link) == 36) and link[0:19] == POKEPASTE


@bot.event
async def on_ready():
    print('bot is online')

@bot.command(name='vrf', help='Runs the teamverify tool on a pokepaste link.')
async def generate_report(ctx,link_arg='oops'):
    #await ctx.send('Message recognized. Test 1 passed!')

    if link_valid(link_arg):
        #await ctx.send('Pokepaste link recognized. Test 2 passed!')
        embed1 = discord.Embed(title='Please wait.',description='This process may take up to a minute...',colour=discord.Colour.green())
        waiting = await ctx.send(embed=embed1)

        team,_ = getTeamString(link_arg,True)
        team2 = teamReasoner(team)
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        _ = teamScore(team2)
        teamReport(team2)

        sys.stdout = old_stdout
        report = mystdout.getvalue()

        embed2 = discord.Embed(description=report,colour=discord.Colour.green())
        embed2.set_author(name='Team Report for '+link_arg)
        await waiting.delete()
        #await ctx.send(str(len(report)))
        await ctx.send(embed=embed2)

    else:
        await ctx.send('Command not recognized. Please use the prefix $vrf, followed by a space, then a pokepaste link.')


#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
    
#    if message.content.startswith('$vrf '):
#        await message.channel.send('Message recognized. Test 1 passed!')
#        paste_link = message.content.split()[1]
        
#        if link_valid(paste_link):
#            await message.channel.send('Pokepaste link recognized. Test 2 passed!')
            #run the actual teamverify process


#    else:
#        await message.channel.send('Command not recognized. Please use the prefix $vrf, followed by a space, then a pokepaste link.')


bot.run(TOKEN)