#8. Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um número ímpar de elementos.
def median(arr):
    # Ordenar o vetor em ordem crescente
    arr.sort()
    
    # Verificar se o vetor tem um número ímpar de elementos
    n = len(arr)
    if n % 2 == 1:
        # Retorna o elemento do meio (índice n//2)
        return arr[n//2]
    else:
        # Retorna a média dos dois elementos do meio (índices n//2 - 1 e n//2)
        return (arr[n//2 - 1] + arr[n//2]) / 2
# ex
arr1 = [1, 3, 5, 7, 9]
print(median(arr1))  # 5

arr2 = [1, 2, 3, 4, 5, 6]
print(median(arr2))  # 3.5

arr3 = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(median(arr3))  # 3