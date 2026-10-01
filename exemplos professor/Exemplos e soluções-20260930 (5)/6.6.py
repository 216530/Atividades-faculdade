'''Receber a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
1 – Janeiro, 2 – Fevereiro, . . . ).
'''

meses = ["Janeiro","Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

media = 0
for i in range(12) :
    temperaturas.append(float(input(f"Informe a temperatura de {meses[i]}: ")))
    media += temperaturas[i]
media = media / 12

print("Meses com temperaturas acima da media anual:")
for i in range(12) :
    if temperaturas[i] > media :
        print(f"{meses[i]} - {temperaturas[i]}")
    
    
    
    