import requests
from bs4 import BeautifulSoup 
from termcolor import colored, cprint
import json
from scrap_zalandoPNLive import *

def imprimir(nombre,SKU,lista_tallas,lista_pid,lista_stock,precio):
    
    print("\n")
    cprint("---------------------------------------------------------------------------------------------------------","yellow")
    cprint("Nombre: ", 'green', attrs=['bold'], end="" )
    cprint(nombre,'blue')

    cprint("SKU: ",'green',attrs=['bold'], end="" )
    cprint(SKU,'blue')

  
    i=0
    for talla in lista_tallas:
        cprint("PID ", 'green', attrs=['bold'], end="" )
        cprint(lista_pid[i], 'blue',end="" )
        
        
        cprint("    Talla ", 'green', attrs=['bold'], end="" )
        cprint(talla,'blue',end="")

        cprint("    Stock ", 'green', attrs=['bold'], end="" )
        if(lista_stock[i]==0):
            cprint('OOS','red')
        else:
            cprint(lista_stock[i],'blue')
        
         
        

        i=i+1
        
    cprint("Precio: ",'green',attrs=['bold'],end="")
    cprint(precio,'blue')


def scrapZalandoPLive(url1):
    # USER AGENT PARA PROTEGERNOS DE BANEOS, LA PAGINA NO NOS IDENTIFIQUE COMO BOT
    headers = { "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"}

    # URL SEMILLA
    url=url1

    # REQUERIMIENTO AL SERVIDOR
    respuesta = requests.get(url, headers=headers)

    # PARSEO DEL ARBOL CON BEAUTIFUL SOUP/ respuesta.text (devuelve codigo html) /lxml se le pasa para que parsee corectamente
    soup = BeautifulSoup(respuesta.text,features="lxml")

    #JSON GLOBAL CON TODOS LOS DATOS
    
    try:
        jsonSoup=soup.find("script",id="z-vegas-pdp-props")
        jsonSoupString = jsonSoup.string
        diccionario = json.loads(jsonSoupString.lstrip('<![CDATA').rstrip(']>')) #con .load, convierto el string que esta en formato JSON, a un objeto diccionario python, pudiendo asi manejarlo y sacar por clave-valor"

      

        #NOMBRE,SKU,PRECIO DENTRO DE JSON
        SKU=diccionario['model']['articleInfo']['id']
        nombre=diccionario['model']['articleInfo']['name']
        precio=diccionario['model']['articleInfo']['units'][0]['price']['formatted']

        #IMAGEN DENTRO DE JSON
        imagen=diccionario['model']['articleInfo']['media']['images'][0]['sources']['zoom']
        
        
        #TALLAS, PID, STOCK DENTRO DE JSON
        desired_data_list = diccionario['model']['articleInfo']['units']              #[0]['size']['local']

    
        lista_tallas=list()
        lista_pid=list()
        lista_stock=list()

        for elem in desired_data_list:
            talla= elem['size']['local'] #el json al transformalrlo a objeto diccionario python, en size, el formato talla esta en string, lo podemos ver en el JSON, asique elem['size']['local'] devuelve string
            pid=elem['id']
            stock=elem['stock']
            lista_stock.append(stock)
            lista_pid.append(pid)
            lista_tallas.append(talla)
            
        imprimir(nombre,SKU,lista_tallas,lista_pid,lista_stock,precio)

        return nombre,SKU,lista_tallas,lista_pid,lista_stock,precio,imagen,None

    
    
    except Exception as e:
        nombre,SKU,precio,imagen,release=scrapZalandoPNLive(url1,soup)
        
        return nombre,SKU,None,None,None,precio,imagen,release

  




    
    
