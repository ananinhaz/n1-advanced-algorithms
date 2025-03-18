import random
import time
import logging
from abc import ABC, abstractmethod
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Configuração do OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)

# Desativar logs excessivos do OpenTelemetry
logging.getLogger("opentelemetry").setLevel(logging.CRITICAL)
logging.getLogger("opentelemetry.sdk").setLevel(logging.CRITICAL)

# Interface para o padrão Strategy
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, arr):
        pass

# Algoritmos de ordenação
class BubbleSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("BubbleSort"):
            n = len(arr)
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                if not swapped:
                    break

class BubbleSortOptimized(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("BubbleSortOptimized"):
            n = len(arr)
            for i in range(n):
                newn = 0
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        newn = j
                if newn == 0:
                    break

class QuickSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("QuickSort"):
            def _quicksort(arr, low, high):
                if low < high:
                    pi = partition(arr, low, high)
                    _quicksort(arr, low, pi - 1)
                    _quicksort(arr, pi + 1, high)

            def partition(arr, low, high):
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    if arr[j] < pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                return i + 1

            _quicksort(arr, 0, len(arr) - 1)

class MergeSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("MergeSort"):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]
                self.sort(left)
                self.sort(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1

class InsertionSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("InsertionSort"):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

class SelectionSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("SelectionSort"):
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

class TimSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("TimSort"):
            arr.sort()

class HeapSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("HeapSort"):
            def heapify(arr, n, i):
                largest = i
                l = 2 * i + 1
                r = 2 * i + 2
                if l < n and arr[l] > arr[largest]:
                    largest = l
                if r < n and arr[r] > arr[largest]:
                    largest = r
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    heapify(arr, n, largest)

            n = len(arr)
            for i in range(n // 2, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

class CountingSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("CountingSort"):
            max_val = max(arr)
            count = [0] * (max_val + 1)
            for num in arr:
                count[num] += 1
            idx = 0
            for num, freq in enumerate(count):
                for _ in range(freq):
                    arr[idx] = num
                    idx += 1

class RadixSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("RadixSort"):
            def counting_sort(arr, exp):
                n = len(arr)
                output = [0] * n
                count = [0] * 10
                for i in range(n):
                    index = arr[i] // exp
                    count[index % 10] += 1
                for i in range(1, 10):
                    count[i] += count[i - 1]
                for i in range(n - 1, -1, -1):
                    index = arr[i] // exp
                    output[count[index % 10] - 1] = arr[i]
                    count[index % 10] -= 1
                for i in range(n):
                    arr[i] = output[i]

            max_val = max(arr)
            exp = 1
            while max_val // exp > 0:
                counting_sort(arr, exp)
                exp *= 10

class ShellSort(SortingStrategy):
    def sort(self, arr):
        with tracer.start_as_current_span("ShellSort"):
            n = len(arr)
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp = arr[i]
                    j = i
                    while j >= gap and arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        j -= gap
                    arr[j] = temp
                gap //= 2