def adicionar_numero(lista, numero):
    lista.append(numero)


def mostrar_lista(lista):
    print("Elementos da lista:", lista)


def calcular_soma(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma


def calcular_maior(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior


numeros = []

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    adicionar_numero(numeros, int(entrada))

if numeros:
    mostrar_lista(numeros)
    print("Soma:", calcular_soma(numeros))
    print("Maior valor:", calcular_maior(numeros))
else:
    print("Nenhum número foi inserido.")