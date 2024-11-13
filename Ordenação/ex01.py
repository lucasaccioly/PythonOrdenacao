#1. Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # Encontre o menor elemento na sublista desordenada
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troque o menor elemento com o primeiro elemento da sublista
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#ex
arr = [5, 2, 8, 3, 1]
arr = selection_sort(arr)
print(arr)  # [1, 2, 3, 5, 8]
