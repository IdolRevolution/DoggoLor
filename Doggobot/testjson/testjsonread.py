import json


arquivo_json = open("cardsj.json", 'r', encoding='utf-8')
nome = json.load(arquivo_json)
arquivo_json.close()

for i in nome:
    print(i["name"])