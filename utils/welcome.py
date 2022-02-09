from utils.profile import Profile
from discord.ext import commands, tasks
from datetime import datetime

import discord
import random

 
class Welcome :
    
    async def welcome_procedure(bot : commands.Bot, member : discord.User) :
        await member.send("Bienvenue sur Balkaland, avant de continuer, laissez-moi finioler votre arrivée")
        await member.send("Quelle est votre couleur préférée ? Veuillez donner sa valeur hexadécimale (le site https://www.color-hex.com/ permet de la trouver)")
        color = await bot.wait_for("message")
        await member.send("Et pour finir votre date de naissance au format jj/mm/aaaa")
        birthday = await bot.wait_for("message")

        profile = Profile(
            username=member.name, 
            id=member.id,
            join=str(datetime.now()),
            birthday=birthday.content, 
            color=color.content,
            secret_id=random.randint(1,10000000)            
        )
        
        profile.to_json()
        user = await bot.fetch_user(profile.id)
        p_embed = discord.Embed(title = profile.username, description = f"A rejoins Balkaland le {profile.join}", color = int(profile.color[1:], 16))
        p_embed.add_field(name='Anniversaire', value=profile.birthday)
        p_embed.add_field(name=f'Secret ID : {profile.secret_id}', value="Ne le partagez surtout pas !")
        p_embed.set_thumbnail(url = user.avatar_url)
        await member.send(embed=p_embed)
        await member.send("Hop c'est fini, bon séjour sur Balkaland")