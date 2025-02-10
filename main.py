from performance_tests import medir_tempo, salvar_resultados_csv
from sorting_algorithms import quicksort, mergesort, bubblesort
from utils import gerar_lista
from grafico import plotar_grafico

def executar_teste(tipo_lista):
    """Executa os testes de desempenho para um tipo específico de lista"""
    tamanhos = [10, 100, 1000, 10000, 50000, 100000, 500000]
    resultados = []

    tempos_quick, tempos_merge, tempos_bubble = [], [], []
    
    for tamanho in tamanhos:
        lista = gerar_lista(tamanho, tipo_lista)

        lista_quick = lista[:]
        lista_merge = lista[:]
        lista_bubble = lista[:]

        # Mede os tempos de execução
        tempo_quick = medir_tempo(quicksort, lista_quick)
        tempo_merge = medir_tempo(mergesort, lista_merge)
        tempos_quick.append(f"{tempo_quick:.6f}")
        tempos_merge.append(f"{tempo_merge:.6f}")

        if tamanho <= 10000: 
            tempo_bubble = medir_tempo(bubblesort, lista_bubble)
            tempos_bubble.append(f"{tempo_bubble:.6f}")
        else:
            tempos_bubble.append("N/A") 

        resultados.append([tamanho, tempos_quick[-1], tempos_merge[-1], tempos_bubble[-1]])

    salvar_resultados_csv(f'resultados_{tipo_lista}.csv', resultados)
    plotar_grafico(tamanhos, tempos_quick, tempos_merge, tempos_bubble, tipo_lista)

def main():
    """Executa os testes para todos os tipos de lista definidos"""
    tipos_de_lista = ['aleatoria', 'ordenada', 'reversa', 'duplicados']
    for tipo in tipos_de_lista:
        executar_teste(tipo)

if __name__ == "__main__":
    main()
