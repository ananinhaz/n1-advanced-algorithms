import random

def gerar_lista(tamanho, tipo):
    """Gera uma lista de números de acordo com o tipo especificado"""
    if tipo == 'aleatoria':
        return [random.randint(0, 10000) for _ in range(tamanho)]
    elif tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'reversa':
        return list(range(tamanho, 0, -1))
    elif tipo == 'duplicados':
        return [random.choice([10, 20, 30, 40, 50]) for _ in range(tamanho)]
