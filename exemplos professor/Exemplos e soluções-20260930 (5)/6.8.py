'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Fulano de Tal
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Fulano de Tal
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

'''
nome = input("Informe o nome do atleta: ")
distancias = list()
ordinais = ["Primeiro","Segundo", "Terceiro", "Quarto", "Quinto"]

for i in range(len(ordinais)) :
    txt = "Informe distancia do {} salto: "
    distancias.append(float(input(txt.format(ordinais[i]))))

txt = ""
media = 0
print("\nResultado final:")
for i in range(len(distancias)) :
    txt += str(distancias[i])
    media += distancias[i]
    # coloca um hifen entre os valores, menos no ultimo
    if i < len(distancias)-1 :
        txt += " - "

print(txt)
txt = "Média dos saltos: {:.2f}"
print(txt.format(media / len(distancias)) )

