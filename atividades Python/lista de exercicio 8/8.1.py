def formatar_data(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    partes = data.split("/")
    if len(partes) != 3 or not all(p.isdigit() for p in partes):
        return None

    dia, mes, ano = int(partes[0]), int(partes[1]), int(partes[2])

    if ano < 1 or mes < 1 or mes > 12 or dia < 1:
        return None

    bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
    limite = 29 if mes == 2 and bissexto else dias_mes[mes - 1]

    if dia > limite:
        return None

    return f"{dia:02d} de {meses[mes - 1]} de {ano:04d}"


print(formatar_data("05/03/2024"))
print(formatar_data("29/02/2023"))
print(formatar_data("31/04/2024"))