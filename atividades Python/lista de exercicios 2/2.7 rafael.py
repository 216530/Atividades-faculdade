'''7. Ler 3 valores inteiros. Verificar se estes valores não formam um triângulo,
neste caso, mostrar mensagem de erro. Caso contrário, apresentar mensagem identificando
o tipo do triângulo formado (isósceles, equilátero ou escaleno).
Para saber mais sobre Triângulos, consultar a wikipedia sobre o assunto.'''


ladoa = int(input("informe o valor do lado a:"))
ladob = int(input("informe o valor do lado b:"))
ladoc = int(input("informe o valor do lado c:"))

tipo = ""
if(ladoa == ladob and ladoa == ladoc and ladob == ladoc) :
    tipo = "equilatero"
elif(ladoa != ladob and ladoa != ladoc and ladob != ladoc) :
    tipo = "escaleno"
else :
    tipo = "isosceles"
    
print(f"triangulo {ladoa}, {ladob},{ladoc} é do tipo {tipo}")