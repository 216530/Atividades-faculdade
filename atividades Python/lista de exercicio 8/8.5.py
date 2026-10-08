def esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True


print(esta_ordenado([1, 2, 3, 4, 5]))
print(esta_ordenado([1, 3, 2, 4]))
print(esta_ordenado([2, 2, 5, 7]))
print(esta_ordenado([]))
print(esta_ordenado([9]))