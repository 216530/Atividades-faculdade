dias = int(input('Informe a quantidade dias: '))

# 1 ano = 365 dias
anos = dias // 365

resto = dias - (anos * 365)

# 30 dias = 1 mes
meses = resto // 30
resto = resto - (meses * 30)

print("Anos: ", anos)
print("Meses: ", meses)
print("Dias: ", resto)
