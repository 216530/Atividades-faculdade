'''
Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo.
Leia o salário e o cargo de um funcionário e calcule o novo salário.
Se o cargo do funcionário não estiver na tabela, ele deverá, então,
receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença.

 Código Cargo Percentual 
101 Gerente 10%
102 Engenheiro 20%
103 Técnico 30%
'''

cargo = int(input('Digite o código de seu cargo:'))
salario = float(input('Informe seu salário:'))

if cargo == 101:
    aumento = salario + (salario * 0.1)
    diferenca = aumento - salario
    print(f'Seu salário antigo era de R${salario}, seu salário novo é de R${aumento}, tendo uma diferença de R${diferenca}')
elif cargo == 102:
    aumento = salario + (salario * 0.2)
    diferenca = aumento - salario
    print(f'Seu salário antigo era de R${salario}, seu salário novo é de R${aumento}, tendo uma diferença de R${diferenca}')
elif cargo == 103:
    aumento = salario + (salario * 0.3)
    diferenca = aumento - salario
    print(f'Seu salário antigo era de R${salario}, seu salário novo é de R${aumento}, tendo uma diferença de R${diferenca}')
else:
    aumento = salario + (salario * 0.4)
    diferenca = aumento - salario
    print(f'Seu salário antigo era de R${salario}, seu salário novo é de R${aumento}, tendo uma diferença de R${diferenca}')
