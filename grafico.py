import matplotlib.pyplot as plt

def plotar_grafico(tamanhos, tempos_quick, tempos_merge, tempos_bubble, tipo_lista):
    """Gera um gráfico comparativo do tempo de execução dos algoritmos de ordenação"""
    plt.figure(figsize=(10, 5))
    plt.plot(tamanhos, tempos_quick, label="QuickSort", marker='o')
    plt.plot(tamanhos, tempos_merge, label="MergeSort", marker='s')
    plt.plot(tamanhos, tempos_bubble, label="BubbleSort", marker='^')

    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title(f'Comparação de Algoritmos - {tipo_lista}')
    plt.legend()
    plt.grid(True)
    plt.show()
