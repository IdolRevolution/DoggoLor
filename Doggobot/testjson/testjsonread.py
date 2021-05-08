import json


class Carta():
    def __init__(self, nome_carta):
        self.nome_carta = nome_carta
        arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
        cardlist = json.load(arquivojson)
        arquivojson.close()


        for cardname in cardlist:
            cardname = (cardname['name'])
            if cardname == self.nome_carta:
                carta_buscada = cardname
                if carta_buscada == True:
                    carta_buscada = self.nome_carta

    def __str__(self):
        return self.link
        
    @property
    def codigocarta(self):
        arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
        cardlist = json.load(arquivojson)
        arquivojson.close()
        

        for codigocarta in self.nome_carta:
            codigocarta = (codigocarta["cardCode"])
            return codigocarta

    @property        
    def setcarta(self):
        arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
        cardlist = json.load(arquivojson)
        arquivojson.close()


        for setcarta in self.nome_carta:
            setcarta = (setcarta["set"])
            return setcarta

    def link(self):
        arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
        cardlist = json.load(arquivojson)
        arquivojson.close()
        setcarta = self.setcarta()
        codigocarta = self.codigocarta()

        return (f'http://dd.b.pvp.net/latest/{setcarta.lower()}/pt_br/img/cards/{codigocarta}.png')


teste = Carta("Garen")
teste.link()

