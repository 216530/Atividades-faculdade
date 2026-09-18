senha = '2023'
conta = 0
while True:
    leitura = input("informe a senha: ")
    conta += 1
    if senha == leitura:
        print(f"Acesso Permitido, após {conta} leituras")
        break
else:
    print("Acesso Negado")