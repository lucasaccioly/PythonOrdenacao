#2. Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que serve como chave para realizar a ordenação crescente ou decrescente.
def sort_with_key(arr, key):
    if key == 'asc':
        return sorted(arr)
    elif key == 'desc':
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Chave de ordenação inválida. Use 'asc' para ordenação crescente ou 'desc' para ordenação decrescente.")
    #ex
arr = [5, 2, 8, 3, 1]

#  crescente
arr_asc = sort_with_key(arr, 'asc')
print(arr_asc)  # [1, 2, 3, 5, 8]

#  decrescente
arr_desc = sort_with_key(arr, 'desc')
print(arr_desc)  # [8, 5, 3, 2, 1]