from performance_tests import medir_tempo, salvar_resultados_csv
from sorting_algorithms import QuickSort, MergeSort, BubbleSort, BubbleSortOptimized, InsertionSort, SelectionSort, TimSort, HeapSort, CountingSort, RadixSort, ShellSort
from utils import gerar_lista
from grafico import plotar_grafico

def executar_teste(tipo_lista):
    """Executa os testes de desempenho para um tipo específico de lista"""
    tamanhos = [10, 100, 1000, 10000, 50000, 100000, 500000]
    resultados = []

    tempos_quick, tempos_merge, tempos_bubble, tempos_bubble_opt, tempos_insertion, tempos_selection, tempos_tim, tempos_heap, tempos_counting, tempos_radix, tempos_shell = [], [], [], [], [], [], [], [], [], [], []

    for tamanho in tamanhos:
        lista = gerar_lista(tamanho, tipo_lista)

        lista_quick = lista[:]
        lista_merge = lista[:]
        lista_bubble = lista[:]
        lista_bubble_opt = lista[:]
        lista_insertion = lista[:]
        lista_selection = lista[:]
        lista_tim = lista[:]
        lista_heap = lista[:]
        lista_counting = lista[:]
        lista_radix = lista[:]
        lista_shell = lista[:]

        # Mede os tempos de execução
        tempo_quick = medir_tempo(QuickSort, lista_quick)
        tempo_merge = medir_tempo(MergeSort, lista_merge)
        tempos_quick.append(f"{tempo_quick:.6f}")
        tempos_merge.append(f"{tempo_merge:.6f}")

        if tamanho <= 10000: 
            tempo_bubble = medir_tempo(BubbleSort, lista_bubble)
            tempos_bubble.append(f"{tempo_bubble:.6f}")
        else:
            tempos_bubble.append("N/A") 

        tempo_bubble_opt = medir_tempo(BubbleSortOptimized, lista_bubble_opt)
        tempos_bubble_opt.append(f"{tempo_bubble_opt:.6f}")
        
        tempo_insertion = medir_tempo(InsertionSort, lista_insertion)
        tempos_insertion.append(f"{tempo_insertion:.6f}")

        tempo_selection = medir_tempo(SelectionSort, lista_selection)
        tempos_selection.append(f"{tempo_selection:.6f}")

        tempo_tim = medir_tempo(TimSort, lista_tim)
        tempos_tim.append(f"{tempo_tim:.6f}")

        tempo_heap = medir_tempo(HeapSort, lista_heap)
        tempos_heap.append(f"{tempo_heap:.6f}")

        tempo_counting = medir_tempo(CountingSort, lista_counting)
        tempos_counting.append(f"{tempo_counting:.6f}")

        tempo_radix = medir_tempo(RadixSort, lista_radix)
        tempos_radix.append(f"{tempo_radix:.6f}")

        tempo_shell = medir_tempo(ShellSort, lista_shell)
        tempos_shell.append(f"{tempo_shell:.6f}")

        resultados.append([tamanho, tempos_quick[-1], tempos_merge[-1], tempos_bubble[-1], tempos_bubble_opt[-1], tempos_insertion[-1], tempos_selection[-1], tempos_tim[-1], tempos_heap[-1], tempos_counting[-1], tempos_radix[-1], tempos_shell[-1]])

    salvar_resultados_csv(f'resultados_{tipo_lista}.csv', resultados)
    # Passando todos os tempos para plotar o gráfico
    plotar_grafico(tamanhos, tempos_quick, tempos_merge, tempos_bubble, tempos_bubble_opt, tempos_insertion, tempos_selection, tempos_tim, tempos_heap, tempos_counting, tempos_radix, tempos_shell, tipo_lista)

def main():
    """Executa os testes para todos os tipos de lista definidos"""
    tipos_de_lista = ['aleatoria', 'ordenada', 'reversa', 'duplicados']
    for tipo in tipos_de_lista:
        executar_teste(tipo)

if __name__ == "__main__":
    main()
