soma = 0
contagem = 0

while True:
    numero = float(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero
    contagem += 1

if contagem > 0:
    media = soma / contagem
    print(f"Quantidade de números informados: {contagem}")
    print(f"Média: {media}")
else:
    print("Nenhum número foi informado.")