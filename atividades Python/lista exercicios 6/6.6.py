meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
temperaturas = []
media = 0
for i in range(12):
    temperaturas.append(float(input(f"Informe a temperatur de {meses[i]}: ")))
    media += temperaturas