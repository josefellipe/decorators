import json

def decorator(funcao):
    file = open('log.csv', '+a')

    def wrapper(*arg, **kwargs):
        parameters = arg
        parameters2 = json.dumps(kwargs)
        response = funcao(*arg, **kwargs)
        result = json.dumps(response)
        file.write(f'{parameters},{parameters2},{result}\n')

        return response

    return wrapper


@decorator
def metodo(name:str):
    print('aqui')
    return f'{name} fazendo as paradas'


def new_function():

    response = metodo('Jose Fellipe')

    print(response)


new_function()