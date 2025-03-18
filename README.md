# Comparação de Algoritmos de Ordenação

Este projeto implementa vários algoritmos de ordenação e analisa seu desempenho em diferentes tipos de listas, utilizando o padrão de design **Strategy** para modularizar a implementação e **OpenTelemetry** para monitoramento e análise de logs. O objetivo é comparar a eficiência dos algoritmos e entender seu impacto em listas de diferentes características e tamanhos.

## Objetivo

O objetivo deste projeto é comparar a eficiência dos seguintes algoritmos de ordenação:

- **QuickSort**
- **MergeSort**
- **BubbleSort**
- **BubbleSort Otimizado**
- **InsertionSort**
- **SelectionSort**
- **HeapSort**
- **TimSort**
- **CountingSort**
- **RadixSort**
- **ShellSort**

Os testes são executados em diferentes cenários para analisar tempo de execução, número de comparações e trocas. As listas testadas variam em tamanho e tipo (aleatórias, ordenadas, reversas e com duplicados).
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
pip install -r requirements.txt
```

### **2️⃣ Executar os Testes**
Para rodar os testes de desempenho e gerar gráficos:

```bash
python main.py
```

Isso executara testes para listas de diferentes tamanhos e características.

---

## Análise de Complexidade

A tabela abaixo mostra a complexidade de tempo e espaço dos algoritmos de ordenação analisados. As complexidades são apresentadas para o melhor caso, caso médio e pior caso, além do uso de espaço auxiliar.

| Algoritmo        | Melhor Caso     | Caso Médio     | Pior Caso      | Espaço Auxiliar  |
|------------------|-----------------|----------------|----------------|------------------|
| **QuickSort**     | O(n log n)      | O(n log n)     | O(n²)          | O(log n) (recursão) |
| **MergeSort**     | O(n log n)      | O(n log n)     | O(n log n)     | O(n) (cópia das listas) |
| **BubbleSort**    | O(n)            | O(n²)          | O(n²)          | O(1)             |
| **BubbleSort Optimized** | O(n)     | O(n²)          | O(n²)          | O(1)             |
| **InsertionSort** | O(n)            | O(n²)          | O(n²)          | O(1)             |
| **SelectionSort** | O(n²)           | O(n²)          | O(n²)          | O(1)             |
| **HeapSort**      | O(n log n)      | O(n log n)     | O(n log n)     | O(1)             |
| **TimSort**       | O(n log n)      | O(n log n)     | O(n log n)     | O(n) (auxílio na mesclagem) |
| **CountingSort**  | O(n + k)        | O(n + k)       | O(n + k)       | O(k)             |
| **RadixSort**     | O(nk)           | O(nk)          | O(nk)          | O(n + k)         |
| **ShellSort**     | O(n log n)      | O(n^(3/2))     | O(n²)          | O(1)             |

---

## Interpretação dos Resultados

- **QuickSort**: Geralmente é o algoritmo mais rápido para listas grandes. No entanto, seu desempenho pode ser prejudicado em casos de listas **quase ordenadas** ou **já ordenadas**, pois o pior caso ocorre quando o pivô é mal escolhido, resultando em \(O(n^2)\). Uma estratégia para evitar esse problema é a escolha de um pivô aleatório.
  
- **MergeSort**: Possui um desempenho estável independentemente da ordenação da lista, com uma complexidade de tempo de \(O(n \log n)\) tanto no melhor quanto no pior caso. No entanto, seu uso de memória é maior, devido à necessidade de alocar espaço auxiliar para as listas durante a fusão.
  
- **BubbleSort**: Embora seja simples de implementar, **BubbleSort** tem um desempenho muito ruim para listas grandes, com complexidade de \(O(n^2)\) tanto no melhor quanto no pior caso. É mais adequado para listas pequenas ou como um algoritmo educativo.
  
- **BubbleSort Otimizado**: A versão otimizada do **BubbleSort** melhora o desempenho ao evitar passagens desnecessárias, mas ainda é \(O(n^2)\) no pior caso. Sua principal melhoria está em detectar se a lista já está ordenada antes de fazer mais passagens.

- **InsertionSort**: **InsertionSort** é eficiente para listas pequenas e já ordenadas, com complexidade de \(O(n)\) no melhor caso. Porém, sua performance decai para \(O(n^2)\) em listas desordenadas.

- **SelectionSort**: Embora simples, **SelectionSort** tem uma complexidade de \(O(n^2)\) em todos os casos e não oferece grandes vantagens sobre outros algoritmos mais eficientes, sendo adequado apenas para listas pequenas.

- **HeapSort**: **HeapSort** tem uma complexidade de \(O(n \log n)\) no melhor, médio e pior caso, e oferece um desempenho relativamente estável em relação aos outros algoritmos.

- **TimSort**: Este algoritmo, usado no Python, é altamente otimizado para listas parcialmente ordenadas e combina as características de **MergeSort** e **InsertionSort**. Seu desempenho é sempre \(O(n \log n)\), mas com melhorias para listas reais.

- **CountingSort**: **CountingSort** é um algoritmo linear (\(O(n + k)\)), mas depende do intervalo de valores dos dados (k). Ele é ideal para listas com números inteiros em um intervalo pequeno.

- **RadixSort**: Embora sua complexidade seja \(O(nk)\), **RadixSort** pode ser eficiente quando o número de dígitos (k) for pequeno, como em listas com números inteiros de tamanho fixo.

- **ShellSort**: **ShellSort** melhora a performance do **InsertionSort** ao realizar comparações em intervalos maiores, mas sua complexidade ainda pode atingir \(O(n^2)\) em alguns casos.

---

## Conclusão

Este projeto demonstrou que a escolha do algoritmo de ordenação pode **impactar drasticamente** o desempenho de uma aplicação, dependendo das características dos dados a serem ordenados.

- **QuickSort** é tipicamente o mais eficiente para listas grandes e aleatórias, mas pode falhar em listas **quase ordenadas** ou **muito desordenadas**. A escolha de um pivô aleatório pode melhorar seu desempenho.
- **MergeSort** oferece uma abordagem mais estável, com complexidade garantida de \(O(n \log n)\), mas usa mais memória, o que pode ser um fator limitante.
- **BubbleSort** e **SelectionSort** devem ser evitados em listas grandes devido à sua ineficiência.
- **TimSort** é extremamente eficiente em listas parcialmente ordenadas, sendo uma excelente escolha quando o desempenho é crucial e os dados têm padrões específicos.
  
Em geral, a escolha do algoritmo deve ser feita com base nas características dos dados e nos requisitos de desempenho da aplicação. A utilização do padrão **Strategy** e a análise com **OpenTelemetry** permitiram uma visão mais profunda dos desempenhos dos algoritmos, auxiliando na escolha do mais adequado para diferentes cenários.

