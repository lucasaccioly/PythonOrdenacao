#6. Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte quantos números pares e quantos números ímpares existem no vetor ordenado.
def sort_and_count(arr):
    # Ordenar o vetor em ordem decrescente
    arr.sort(reverse=True)
    
    # Inicializar contadores para números pares e ímpares
    even_count = 0
    odd_count = 0
    
    # Iterar sobre o vetor ordenado
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Retorna os contadores
    return even_count, odd_count
#ex
arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
even_count, odd_count = sort_and_count(arr1)
print(f"Vetor ordenado: {arr1}")
print(f"Números pares: {even_count}, Números ímpares: {odd_count}")

arr2 = [2, 4, 6, 8, 10]
even_count, odd_count = sort_and_count(arr2)
print(f"Vetor ordenado: {arr2}")
print(f"Números pares: {even_count}, Números ímpares: {odd_count}")

arr3 = [1, 3, 5, 7, 9]
even_count, odd_count = sort_and_count(arr3)
print(f"Vetor ordenado: {arr3}")
print(f"Números pares: {even_count}, Números ímpares: {odd_count}")