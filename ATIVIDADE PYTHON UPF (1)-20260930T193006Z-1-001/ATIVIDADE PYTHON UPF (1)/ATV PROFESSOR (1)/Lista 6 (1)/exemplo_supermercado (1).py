supermercado = []
while True :
    item = input("Informe item a comprar (vazio para terminar): ")

    # testa condicao de parada
    #if item == "" :
    #    break

    # testa condicao de parada de outra forma
    if len(item) == 0 :
        break

    # adiciona um item na lista
    supermercado.append(item)

print("Lista supermercado: ", supermercado)