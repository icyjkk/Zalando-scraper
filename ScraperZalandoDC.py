import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
from scrap_zalandoPLive import *
from scrap_zalandoPNLive import *
import datetime




def imprimirListas(lista):
    elem=" "
    
    for x in lista:
        elem= elem + str(x) +"\n"
      
    return elem   

def imprimirListaStock(lista):
    elem=" "
    
    for x in lista:
        if ( x==0):
            elem= elem + str(x) +"   :red_circle: \n"
        else:
            elem= elem + str(x) +"\n"
    return elem   


""" def imprimirCSVformat(lista):
    elem=" "
    
    for x in lista:
        elem= elem + str(x) + ","
    return elem  """ 

load_dotenv()                         #Estas dos lineas son para cargar el token y tener mas seguridad
TOKEN = os.getenv('DISCORD_TOKEN')    #Carga el token de nv


                                      #Dentro del modulo commands pillamos la funcion Bot, que devuelte un bot
bot= commands.Bot(command_prefix='!') #Prefijo para invocar al bot en discord


@bot.command(name='zalando')
async def zalando(ctx,url):
    
    channel = bot.get_channel(818634786825961532) #Nos devuelve el canal asociado al id de discord, con este chanel podemos enviarle cosasS
    
    
    
    nombre,SKU,lista_tallas,lista_pid,lista_stock,precio,imagen,release=scrapZalandoPLive(url)

        
    if(lista_tallas==None or lista_pid==None or lista_stock==None):

        embed = discord.Embed(title=nombre,url=url,description="Product SKU: " + "`"+ SKU + "`" + "\nPrecio: " + "`"+ precio  + "`"  ,timestamp=datetime.datetime.utcnow(), color=242424)
        
        embed.add_field(name="Release Date", value=release,inline=True)
        embed.set_thumbnail(url=imagen)
        embed.set_footer(text='ZalandoScraper | ',icon_url="http://assets.stickpng.com/images/5a32a860cb9a85480a628f95.png") # set footer
    
        
        
        await channel.send(embed=embed)

        
    else:

        embed = discord.Embed(title=nombre,url=url,description="Product SKU: " + "`"+ SKU + "`" + "\nPrecio: " + "`"+ precio  + "`"  ,timestamp=datetime.datetime.utcnow(), color=242424)
            
        embed.add_field(name="Sizes", value=imprimirListas(lista_tallas),inline=True)
        embed.add_field(name="PIDs",  value=imprimirListas(lista_pid),inline=True)
        embed.add_field(name="Stock", value=imprimirListaStock(lista_stock),inline=True)
        #embed.add_field(name="CSV Format", value="`"+ imprimirCSVformat(lista_pid)+ "`",inline=False)

            
        
        embed.set_thumbnail(url=imagen)
        embed.set_footer(text='ZalandoScraper | ',icon_url="http://assets.stickpng.com/images/5a32a860cb9a85480a628f95.png") # set footer
        
        
        await channel.send(embed=embed)

    
        
    
        
    



@bot.command()
async def ping(ctx):
    response= "`Pong` \n"+ str(round(bot.latency * 1000)) + " ms"
    await ctx.send(response)


bot.run(TOKEN)