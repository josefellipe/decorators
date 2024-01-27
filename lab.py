import json

def decorator(funcao):
    file = open('log.csv', '+a')

    def wrapper(*arg, **kwargs):
        parameters = arg
        parameters2 = json.dumps(kwargs)
        result = json.dumps(funcao(*arg, **kwargs))
        file.write(f'{parameters},{parameters2},{result}')
    return wrapper

@decorator
def metodo(name:str):
    return f'{name} fazendo as paradas'


metodo('Jose Fellipe')