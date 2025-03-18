import matplotlib.pyplot as plt

def plotar_grafico(tamanhos, tempos_quick, tempos_merge, tempos_bubble, tempos_bubble_opt, tempos_insertion, tempos_selection, tempos_tim, tempos_heap, tempos_counting, tempos_radix, tempos_shell, tipo_lista):
    """Gera um gráfico comparativo do tempo de execução dos algoritmos de ordenação"""
    plt.figure(figsize=(10, 5))
    plt.plot(tamanhos, tempos_quick, label="QuickSort", marker='o')
    plt.plot(tamanhos, tempos_merge, label="MergeSort", marker='s')
    plt.plot(tamanhos, tempos_bubble, label="BubbleSort", marker='^')
    plt.plot(tamanhos, tempos_bubble_opt, label="BubbleSortOptimized", marker='x')
    plt.plot(tamanhos, tempos_insertion, label="InsertionSort", marker='d')
    plt.plot(tamanhos, tempos_selection, label="SelectionSort", marker='p')
    plt.plot(tamanhos, tempos_tim, label="TimSort", marker='h')
    plt.plot(tamanhos, tempos_heap, label="HeapSort", marker='v')
    plt.plot(tamanhos, tempos_counting, label="CountingSort", marker='*')
    plt.plot(tamanhos, tempos_radix, label="RadixSort", marker='+')
    plt.plot(tamanhos, tempos_shell, label="ShellSort", marker='1')

    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title(f'Comparação de Algoritmos - {tipo_lista}')
    plt.legend()
    plt.grid(True)
    plt.show()