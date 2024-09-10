import json

with open("dados.json", "r") as arquivo_json:
    data = json.load(arquivo_json)
    
print(data)