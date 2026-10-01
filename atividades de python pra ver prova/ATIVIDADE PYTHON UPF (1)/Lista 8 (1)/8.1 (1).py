'''
1. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato DD de MÊS de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

def converter_data(ddmmyyyy):
    mes = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
    
    dd = ddmmyyy[:2]
    
    mm = int(ddmmyyyy[3:5])
    
    yyyy = ddmmyyyy[6:10]
    
    return dd + 'de' + mes[mm-1] + 'de' + yyyy

print(converter_data('23/10/2023'))