dia = int(input("Informe o dia da semana (1 - 7): "))

if dia == 1:
   diaSemana = "Domingo"
elif dia == 2:
   diaSemana = "Segunda-Feira"
elif dia == 3:
   diaSemana = "Terça-Feira"
elif dia == 4:
   diaSemana = "Quarta-Feira"
elif dia == 5:
   diaSemana = "Quinta-Feira"
elif dia == 6:
   diaSemana = "Sexta-Feira"
elif dia == 7:
   diaSemana = "Sábado"
else:
   diaSemana = "Dia inválido"

print(diaSemana)