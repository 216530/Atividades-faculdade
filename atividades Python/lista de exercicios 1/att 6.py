#6. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
#cada qual sendo vendido respectivamente por 10, 12 e 15 reais.
#Implemente um programa em que o usuário forneça a quantidade de camisetas pequenas,
#médias e grandes referentes a uma venda e retorne o valor a ser cobrado.

pequena = int(input('informe a quantidade de camisetas pequenas'))
media = int(input('informe a quantidade de camisetas medias'))
grande = int(input('informe a quantidade de camisetas grandes'))
x,y,z = (pequena * 10), (media * 12), (grande *15)
 
print(f'{x} o valor é: ,{y} o valor é:  ,{z}o valor é: ')