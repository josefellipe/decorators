from lab import decorator


@decorator
def teste_soma(a:int, b:int, c:dict):
    if c.get('operation') == 'sum':
        return a+b
    return a-b


print(teste_soma(1,3, {'operation': 'sum'}))