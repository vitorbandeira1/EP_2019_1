import json
def carregar_cenarios():
    with open('cenarios.json','r')as arquivo:
        texto=arquivo.read()
    cenarios=json.loads(texto)
