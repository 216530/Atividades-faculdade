# grava números em um arquivo

numeros = list()

while True :
    n = int(input("Informe um número, zero para parar: "))
    
    if n == 0 :
        break
    
    numeros.append(n)

# grava lista em um arquivo
arquivo = open("dados.txt", "w")
for x in numeros :
    arquivo.write(str(x) + "\n")
arquivo.close()











