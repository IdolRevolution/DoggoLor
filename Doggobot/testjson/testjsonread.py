import json


arquivojson = open('C:desktop/lore/cardsj.json', 'r', encoding='utf-8')
nome = json.load(arquivojson)
arquivojson.close()

for i in nome:
    print(i["name"])