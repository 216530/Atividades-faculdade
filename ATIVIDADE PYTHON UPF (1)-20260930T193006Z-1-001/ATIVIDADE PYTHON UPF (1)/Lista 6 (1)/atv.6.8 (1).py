'''
8. Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do
programa deve ser conforme o exemplo abaixo:

Atleta: Thiago Braz
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Thiago Braz
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

ordem = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

while True:
    nome = input("Atleta (deixe vazio para sair): ")
    
    if not nome:
        break
        
    saltos = []
    
    for i in range(5):
        distancia = float(input(f"{ordem[i]} Salto: "))
        saltos.append(distancia)
    
    media = sum(saltos) / len(saltos)
    
    saltos_texto = " - ".join(map(str, saltos))

    print("\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos_texto}")
    print(f"Média dos saltos: {media:.1f} m")







