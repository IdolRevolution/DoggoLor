import json


arquivojson = open('set1-pt_br.json', 'r', encoding='utf-8')
cardlist = json.load(arquivojson)
arquivojson.close()

for dicionario in cardlist:
    if "Garen" in dicionario.values():
        assets = dicionario["assets"]
        for item in assets:
            item = item["gameAbsolutePath"]
            print(item)

