# funcao que converte uma data e retorna em um formato por extenso
def dataPorExtenso (ddmmyyyy):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio",\
             "junho", "julho", "agosto", "setembro", "outubro",\
             "novembro", "dezembro"]
    dd = ddmmyyyy[:2]
    mm = int(ddmmyyyy[3:5])
    yyyy = ddmmyyyy[6:10]
    
    return dd + " de " + meses[mm-1] + " de " + yyyy

# comentário da função seguinte ...

