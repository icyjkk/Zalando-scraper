import requests
from bs4 import BeautifulSoup 
from termcolor import colored, cprint

def imprimir2(nombre,SKU,precio,release):

    print("\n")
    cprint("---------------------------------------------------------------------------------------------------------","yellow")
    cprint("Nombre: ", 'green', attrs=['bold'], end="" )
    cprint(nombre,'blue')

    cprint("SKU: ",'green',attrs=['bold'], end="" )
    cprint(SKU,'blue')

    cprint("Precio: ",'green',attrs=['bold'], end="" )
    cprint(precio,'blue')

    cprint("Release Date: ",'green',attrs=['bold'], end="" )
    cprint(release,'blue')

def scrapZalandoPNLive(url1,soup):


    #NOMBRE
    nombre=soup.find('h1',class_='OEhtt9 ka2E9k uMhVZi z-oVg8 pVrzNP w5w9i_ _1PY7tW _9YcI4f').text

    #SKU
    lista_soup_sku=soup.find('div',attrs={"data-testid":"pdp-accordion-details"}).findAll('span', class_='u-6V88 ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP zN9KaA')
    length=len(lista_soup_sku)
    SKU=lista_soup_sku[length-1].text

    #PRECIO
    precio=soup.find('span',class_='uqkIZw ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP').text
    
    
    #Imagen
    imagen=soup.find('img',class_='_6uf91T z-oVg8 u-6V88 ka2E9k uMhVZi FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF PZ5eVw')
    imagen=imagen['src'] #Asi saco el valor del atributo src

    #Release Date
    release=soup.find('h2',class_='AKpsL5 ka2E9k uMhVZi z-oVg8 pVrzNP').text
    

    imprimir2(nombre,SKU,precio,release)
    
    return nombre,SKU,precio,imagen,release
 
