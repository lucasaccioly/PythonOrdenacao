#4. Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
def second_smallest(arr):
    unique_elements = list(set(arr))  # Remove duplicates
    unique_elements.sort()  # Sort the list in ascending order
    
    if len(unique_elements) < 2:
        raise ValueError("O vetor deve ter pelo menos dois elementos únicos.")
    
    return unique_elements[1]
#ex
arr1 = [5, 2, 8, 3, 1]
print(second_smallest(arr1))  # 2

arr2 = [1, 1, 2, 3, 4]
print(second_smallest(arr2))  # 2

arr3 = [1, 1, 1]
try:
    print(second_smallest(arr3))
except ValueError as e:
    print(e)  #  deve ter pelo menos dois elementos únicos.