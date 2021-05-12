import json


arquivojson = open('finaljson.json', 'r', encoding='utf-8')
cardlist = json.load(arquivojson)
arquivojson.close()


def find_card(carta):
    for dicionario in cardlist:
        if carta in dicionario.values():
            assets = dicionario["assets"]
            for item in assets:
                item = item["gameAbsolutePath"]
                print(item)

find_card("Yasuo")
