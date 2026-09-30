'''
6. Receber a temperatura média de cada mês do ano e armazene-as
em uma lista. Após isto, calcule a média anual das temperaturas
e mostre todas as temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). 
'''

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = []
soma_temperaturas = 0

print("Digite a temperatura média de cada mês:")
for i in range(12):
    temp = float(input(f"Temperatura de {meses[i]}: "))
    temperaturas.append(temp)
    soma_temperaturas += temp

media_anual = soma_temperaturas / 12

print(f"Média Anual das Temperaturas: {media_anual:.2f}°C")

print("Meses com temperaturas acima da média:")

for i in range(12):
    if temperaturas[i] > media_anual:
        
        print(f"{i + 1} - {meses[i]}: {temperaturas[i]}°C")
        
        
        


