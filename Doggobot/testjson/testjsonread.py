import json


arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
nome = json.load(arquivojson)
arquivojson.close()

for codigocarta in nome:
    codigo1 = (codigocarta["cardCode"])
    
for setcarta in nome:
    cardset1 = (setcarta["set"])

codigo = (f'http://dd.b.pvp.net/latest/{cardset1.lower()}/pt_br/img/cards/{codigo1}.png')

print(codigo)