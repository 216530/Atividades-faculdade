'''
2. Elabore uma função que converta um horário 24 horas para a notação de 12 horas.
Por exemplo, a função deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
'''


def horario(h, m):
    if h > 12:
        hr = h - 12
        sufixo = 'P.M'
        
    else:
        hr = h
        sufixo = 'A.M'
    txt = str(hr)+ ':'+str(m)+sufixo
    

        
        