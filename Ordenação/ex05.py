#5. Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos duplicados, retornando o vetor resultante sem duplicatas. Não é perimitido utilizar a função “set()”
def remove_duplicates(arr):
    result = []
    
    for element in arr:
        if element not in result:
            result.append(element)
    
    return result
#ex
arr1 = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr1))  # [1, 2, 3, 4, 5]

arr2 = [1, 1, 1, 2, 2, 3]
print(remove_duplicates(arr2))  # [1, 2, 3]

arr3 = [5, 5, 5, 5]
print(remove_duplicates(arr3))  # [5]