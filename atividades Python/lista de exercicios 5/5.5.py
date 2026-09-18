positivos = 0
negativos = 0

for i in range (10):
    valor = int(input("digite um valor:"))

if valor > 0:
    positivos += 1
elif valor < 0:
    negativos += 1
else :
    print("informado zero! ")
    print(f"positivos: {positivos} Negativos: {negativos}")