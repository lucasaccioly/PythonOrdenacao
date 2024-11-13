#3. Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.
def find_max_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    
    for element in arr:
        if element > max_element:
            max_element = element
        elif element < min_element:
            min_element = element
    
    return max_element, min_element
#ex
arr = [5, 2, 8, 3, 1]
max_element, min_element = find_max_min(arr)
print(f"Máximo: {max_element}, Mínimo: {min_element}")  # mxm: 8, mnm: 1