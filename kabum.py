#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

# inicio
url="https://www.kabum.com.br/"
    
#headers = {'Content-Type': 'application/html','From':'seuemail@email.com.br','Accept-Language': 'pt-BR'}
pagina = requests.get(url).text

conteudo = BeautifulSoup(pagina, features='html.parser')

print("URL: "+url)

linhas = conteudo.findAll('script')

for linha in linhas:


    if(str( linha).find("dataLayer") > -1 ) :
        #print("ACHEIII !!!!")

        # Termina no ; (ponto e virgula)
        jsonKabum = str(linha).split(';')[0]

        # pega o que vem depois do primeiro [ (abre colchetes) até o fim da string
        jsonKabum = jsonKabum.split('{')[1:]
        

        for item in jsonKabum :
            itemPronto = item.split('}')[0]

            
            if itemPronto.find('"name"') > -1 and itemPronto.find('"category"') > -1 and itemPronto.find('"price"') > -1 and itemPronto.find('"available"') > -1 :
                
                print("------------------------------")
                print("ITEM: " + itemPronto )

                # Pega o que tem depois de "name"
                itemName = itemPronto.split('"name"')[1]

                # Pega o conteudo de name que esta entre " (aspas duplas)
                itemName = itemName.split('"')[1]
                
                print("NAME: "+ itemName)
                
                itemId = itemPronto.split('"id"')[1]


                itemId = itemId.split('"')[1]

                print("ID: "+itemId)

                print("URL: "+ "https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo="+itemId)
                itemPrice = itemPronto.split('"price"')[1]

                # Pega o conteudo de price que esta depois de : (dois pontos)
                itemPrice = itemPrice.split(':')[1]

                # Pega o conteudo até antes da virgula
                itemPrice = itemPrice.split(',')[0]

                print("PRICE: "+itemPrice)

                # Pega o que tem depois de "available"
                itemAvailable = itemPronto.split('"available"')[1]

                # Pega o conteudo de available que vem vem depois de : (dois pontos) e remove os espaços em branco do final
                itemAvailable = itemAvailable.split(':')[1].strip()

                print("AVAILABLE: "+ itemAvailable)

                print("------------------------------")


        exit(0)
