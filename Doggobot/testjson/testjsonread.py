import json


arquivojson = open("cardsj.json", 'r', encoding='utf-8')
nome = json.load(arquivojson)
arquivojson.close()

for i in nome:
    print(i["name"])