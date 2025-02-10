# Comparação de Algoritmos de Ordenação

Este projeto implementa três algoritmos de ordenação e analisa seu desempenho em diferentes tipos de listas.

## Objetivo

O objetivo do projeto é comparar a eficiência dos seguintes algoritmos de ordenação:

- **QuickSort**
- **MergeSort**
- **BubbleSort**

Os testes são executados em diferentes cenários para analisar tempo de execução e impacto em listas com características distintas.

---

## Estrutura do Projeto

```
📂 Desafio-2
│── 📄 main.py               # Executa os testes e gera gráficos
│── 📄 sorting_algorithms.py # Implementação dos algoritmos
│── 📄 performance_tests.py  # Mede o tempo de execução
│── 📄 utils.py              # Geração de listas de teste
│── 📄 grafico.py            # Geração de gráficos
│── 📄 README.md             # Documentação do projeto
```

---

## Como Executar

### **1️⃣ Instalar Dependências**
Verifique de ter o Python instalado e instale a biblioteca necessária:

```bash
pip install matplotlib
```

### **2️⃣ Executar os Testes**
Para rodar os testes de desempenho e gerar gráficos:

```bash
python main.py
```

Isso executara testes para listas de diferentes tamanhos e características.

---

## Análise de Complexidade

| Algoritmo   | Melhor Caso  | Caso Médio  | Pior Caso   | Espaço Auxiliar  |
|------------|-------------|-------------|------------|-----------------|
| **QuickSort**  | O(n log n)   | O(n log n)   | O(n²)       | O(log n) (recursão) |
| **MergeSort**  | O(n log n)   | O(n log n)   | O(n log n)  | O(n) (devido à cópia das listas) |
| **BubbleSort** | O(n)         | O(n²)        | O(n²)       | O(1) |

---

## Interpretação dos Resultados

- **QuickSort** geralmente o mais rápido, mas pode ser ineficiente para listas **já ordenadas** devido ao seu pior caso O(n²).
- **MergeSort** tem desempenho estável **independente da ordem da lista**, mas usa mais memória.
- **BubbleSort** é **ineficiente para listas grandes** e só deve ser usado para pequenas entradas.

---

## Melhorias Possíveis

- **Otimizar QuickSort** escolhendo um **pivô aleatório** para evitar o pior caso.
- **Implementar HeapSort** como uma alternativa eficiente ao MergeSort e QuickSort.
- **Testar mais cenários** com diferentes distribuições de números.

---

## Conclusão

Este projeto demonstra como a escolha do algoritmo certo **impacta drasticamente** o desempenho. QuickSort é geralmente a melhor escolha, mas MergeSort é mais confiável quando não queremos depender de heurísticas de pivô. BubbleSort deve ser evitado para grandes volumes de dados.
