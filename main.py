from contextlib import nullcontext
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions

from utils.profile import *
from utils.welcome import Welcome
from utils.karaokOS import *

import discord 
import json

with open("data/profile", 'r', encoding='utf8') as config :
    config = json.load(config)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_member_join(member : discord.User):
    await Welcome.welcome_procedure(bot,member)

@bot.command('balkabot')
async def balkabot(ctx : commands.Context):
    await ctx.send("Salut !\nJe suis balkabot, bot dédié à Balkaland V.3. Pour la liste des commandes : `$help`")

@bot.command('profil')
async def profil(ctx : commands.Context, username):    
    result = get_profile(username)      
    if result != None  :
        user = await bot.fetch_user(result.id)
        p_embed = discord.Embed(title = username, description = f"A rejoins Balkaland le {result.join}", color = int(result.color[1:], 16))
        p_embed.add_field(name='Anniversaire', value=result.birthday)
        p_embed.set_thumbnail(url = user.avatar_url)
        await ctx.send(embed=p_embed)
    else :
        await ctx.send("Profil introuvable")

@bot.command('clear')
@has_permissions(administrator = True)
async def clear(ctx : commands.Context, number):    
    msg = []
    number = int(number)
    async for message in ctx.history(limit = number) :
        await message.delete()

@bot.command('karaoke')
async def karaoke(ctx : commands.Context) :
    await ctx.send("D'humeur chanteuse ? :microphone: Pas de souci...démarrage de KaraokOS")
    await ctx.send("L'artise :")
    artist = await bot.wait_for('message')
    await ctx.send("Le titre :")
    song = await bot.wait_for('message')
    result = search_lyrics(artist.content, song.content)
    if result == None :
        await ctx.send("Pas de paroles trouvées")
    else :
        await ctx.send(result)
        

bot.run(config['key'])