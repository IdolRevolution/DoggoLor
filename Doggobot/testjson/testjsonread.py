import json


arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
cardlist = json.load(arquivojson)
arquivojson.close()


lista = [{"pinto":"Renan", "rola":"Paulo"}, {"pinto":"Guto", "rola":"Fernando"}]

for dicionario in lista:
    nome = dicionario["pinto"]
    if nome in dicionario:
        print(nome)

    name = name["rola"]



    if name in :
        for nome in lista:
            nome = nome["pinto"]
            print(name, nome)
    else:
        print("Erro")



def buscacarta():
    for cardname in cardlist:
        cardname = cardname["name"]
        return cardname




def codigocarta():
    carta = buscacarta()
    for codigocarta in carta:
        codigocarta = codigocarta["cardCode"]
        print(codigocarta)

         
def setcarta():
    carta = buscacarta()
    for setcarta in carta:
        setcarta = setcarta["set"]
        print(setcarta.lower())

def link():

    print(f'http://dd.b.pvp.net/latest/{setcarta()}/pt_br/img/cards/{codigocarta()}.png')

link()



