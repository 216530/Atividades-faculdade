def contar_letras(frase):
    contagem = {}

    for letra in frase:
        if letra.isalpha():
            letra = letra.upper()
            if letra in contagem :
                contagem[letra] += 1
            else:
                contagem[letra] = 1
        return contagem
frase_entrada = input("Digite uma frase paa contar as letras")
resultado_contagem = contar_letras(frase_entrada)
print("contagem de letras: ")
for letra, quantidade in resultado_contagem.items():
    print(f"{letra}: {quantidade}")
print("Como esta armazenado: ", resultado_contagem)
