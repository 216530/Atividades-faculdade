'''5. Sistema de reservas de um cinema
Um cinema deseja desenvolver um programa para controlar a ocupação de uma sala com 8 fileiras e 10 assentos por fileira. O sistema deverá utilizar uma matriz para representar os assentos, considerando 0 para assento disponível e 1 para assento ocupado.
O programa deverá apresentar um menu com as seguintes opções:
1. Exibir mapa de assentos: apresentar a situação de todos os assentos da sala.
2. Reservar assento: solicitar a fileira e o número do assento, verificando se ele está disponível antes de realizar a reserva.
3. Cancelar reserva: permitir liberar um assento previamente reservado.
4. Consultar ocupação: informar a quantidade e o percentual de assentos ocupados e disponíveis.
5. Verificar fileira: informar quantos assentos estão disponíveis em uma determinada fileira.
6. Encerrar: finalizar o programa.'''


sala = []
for i in range(8):
    fileira = []
    for j in range(10):
        fileira.append(0)
    sala.append(fileira)

opcao = 0
while opcao != 6:
    print("\n1 - Exibir mapa de assentos")
    print("2 - Reservar assento")
    print("3 - Cancelar reserva")
    print("4 - Consultar ocupação")
    print("5 - Verificar fileira")
    print("6 - Encerrar")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n     ", end="")
        for j in range(10):
            print(j + 1, end=" ")
        print()
        for i in range(8):
            print("F", i + 1, " ", end="")
            for j in range(10):
                print(sala[i][j], end=" ")
            print()

    elif opcao == 2:
        f = int(input("Fileira (1 a 8): "))
        a = int(input("Assento (1 a 10): "))
        if f < 1 or f > 8 or a < 1 or a > 10:
            print("Fileira ou assento inválido.")
        elif sala[f - 1][a - 1] == 1:
            print("Assento já está ocupado.")
        else:
            sala[f - 1][a - 1] = 1
            print("Reserva realizada com sucesso.")

    elif opcao == 3:
        f = int(input("Fileira (1 a 8): "))
        a = int(input("Assento (1 a 10): "))
        if f < 1 or f > 8 or a < 1 or a > 10:
            print("Fileira ou assento inválido.")
        elif sala[f - 1][a - 1] == 0:
            print("Esse assento não está reservado.")
        else:
            sala[f - 1][a - 1] = 0
            print("Reserva cancelada com sucesso.")

    elif opcao == 4:
        ocupados = 0
        for i in range(8):
            for j in range(10):
                if sala[i][j] == 1:
                    ocupados += 1
        livres = 80 - ocupados
        print("Ocupados:", ocupados, "-", ocupados / 80 * 100, "%")
        print("Disponíveis:", livres, "-", livres / 80 * 100, "%")

    elif opcao == 5:
        f = int(input("Fileira (1 a 8): "))
        if f < 1 or f > 8:
            print("Fileira inválida.")
        else:
            livres = 0
            for j in range(10):
                if sala[f - 1][j] == 0:
                    livres += 1
            print("Assentos disponíveis na fileira", f, ":", livres)

    elif opcao == 6:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")