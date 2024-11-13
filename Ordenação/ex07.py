#7. Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número. Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
def third_largest(arr):
    # remover duplicatas
    unique_arr = []
    for element in arr:
        if element not in unique_arr:
            unique_arr.append(element)
    
    # ordem decrescente
    unique_arr.sort(reverse=True)
    
    # vetor tem pelo menos 3 elementos
    if len(unique_arr) < 3:
        return None
    
    # Retorna o terceiro maior número
    return unique_arr[2]
#ex
arr1 = [1, 2, 3, 4, 5]
print(third_largest(arr1))  # 3

arr2 = [5, 5, 5, 5]
print(third_largest(arr2))  # None

arr3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(third_largest(arr3))  # 3