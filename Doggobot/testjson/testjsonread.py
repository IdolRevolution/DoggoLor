import json


arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
nome = json.load(arquivojson)
arquivojson.close()

for i in nome:
    print(i["name"])