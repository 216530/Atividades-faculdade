'''
Leia o salário e o cargo de um funcionário e calcule
o novo salário.

Código 	Cargo	 Percentual 
101	Gerente	10%
102	Engenheiro	20%
103	Técnico	30%
Se o cargo do funcionário não estiver na tabela, ele deverá,
então, receber 40% de aumento.
Mostre o salário antigo, o novo salário e a diferença.
'''

salario = float(input("Informe o salario do funcionario: "))
cargo = int(input("Informe o cargo do funcionario: "))

if cargo == 101 :
    salarioNovo = salario * 1.1
elif cargo == 102 :
    salarioNovo = salario * 1.2
elif cargo == 103 :
    salarioNovo = salario * 1.3
else :
    salarioNovo = salario * 1.4

diferenca = salarioNovo - salario
txt = "O salario antigo era {}, o novo ficou {} com diferenca de {}"; 
print(txt.format(salario,salarioNovo,diferenca))
