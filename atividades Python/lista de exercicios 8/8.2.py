def converter_horario(hora, minuto):
    periodo = "A.M." if hora < 12 else "P.M."
    hora12 = hora % 12
    if hora12 == 0:
        hora12 = 12
    return f"{hora12}:{minuto:02d} {periodo}"


print(converter_horario(14, 25))
print(converter_horario(0, 5))
print(converter_horario(12, 0))
print(converter_horario(9, 30))