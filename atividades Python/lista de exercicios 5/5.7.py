conta = 0
while conta <= 10:
    valor =int(input("informe um valor: "))
    if valor == 0:
        print("Zero informado! ")
        continue
    elif valor > 0:
        print("numero positivo! ")
    else:
        print("numero negativo! ")
    conta += 1

    print(f"foram lidos {conta} numeros")