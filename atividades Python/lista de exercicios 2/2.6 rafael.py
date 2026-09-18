'''6. Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Leia o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença. 

 Código 	Cargo	 Percentual 
101	Gerente	10%
102	Engenheiro	20%
103	Técnico	30%
'''

salario = float(input("informe o salario do funcionario:" ))
cargo= input("informe o nome do cargo do funcionario:" )

if cargo == 101 :
    salarioNovo = salario * 1.1
elif cargo == 102:
        salarioNovo = salario * 1.2
elif cargo == 103 :
    salarioNovo - salario * 1.3
else :
    salarioNovo = salario * 1.4

diferenca = salarioNovo - salario
print(f"O salario antigo era {salario}, o novo ficou {salarioNovo} com diferença de {diferenca}")