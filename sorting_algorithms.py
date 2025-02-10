def quicksort(arr):
    """Ordena a lista utilizando QuickSort in-place"""
    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    def partition(arr, low, high):
        """Função auxiliar que escolhe um pivô e reorganiza a lista."""
        pivot = arr[high]  # Pivô escolhido como o último elemento
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quicksort(arr, 0, len(arr) - 1)

def mergesort(arr):
    """Ordena a lista utilizando MergeSort in-place"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        # Combina as listas ordenadas
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

def bubblesort(arr):
    """Ordena a lista utilizando BubbleSort"""
    n = len(arr)
    for i in range(n):
        troca = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca = True
        if not troca:
            break  
