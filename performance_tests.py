import time
import csv

def medir_tempo(funcao, arr):
    """Mede o tempo de execução de uma função de ordenação"""
    inicio = time.time()
    funcao().sort(arr)
    fim = time.time()
    return fim - inicio

def salvar_resultados_csv(nome_arquivo, dados):
    """Salva os resultados dos testes de desempenho em um arquivo CSV"""
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tamanho", "QuickSort", "MergeSort", "BubbleSort", "BubbleSortOptimized", 
                         "InsertionSort", "SelectionSort", "TimSort", "HeapSort", "CountingSort", 
                         "RadixSort", "ShellSort"])
        writer.writerows(dados)