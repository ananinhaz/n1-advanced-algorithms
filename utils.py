import random

def gerar_lista(tamanho: int, tipo: str):
    """Gera uma lista de números de acordo com o tipo especificado"""
    if tipo == 'aleatoria':
        return [random.randint(0, 10000) for _ in range(min(tamanho, 10000))]  # Limitando a 10.000 elementos
    elif tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'reversa':
        return list(range(tamanho, 0, -1))
    elif tipo == 'duplicados':
        return [random.choice([1, 2, 3, 4]) for _ in range(tamanho)]
    return []