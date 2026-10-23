alunos = {
    "Ana": {"nota1": 8.5, "nota2": 7.0},
    "Bruno": {"nota1": 5.0, "nota2": 6.5},
    "Carla": {"nota1": 9.0, "nota2": 9.5},
    "Diego": {"nota1": 6.0, "nota2": 4.5},
    "Eduardo": {"nota1": 8.0, "nota2": 6.0},
    "Fernanda": {"nota1": 7.5, "nota2": 8.0},
    "Gabriel": {"nota1": 4.0, "nota2": 5.5},
    "Helena": {"nota1": 9.5, "nota2": 8.5},
    "Igor": {"nota1": 6.5, "nota2": 7.0},
    "Juliana": {"nota1": 8.0, "nota2": 9.0},
    "Lucas": {"nota1": 3.5, "nota2": 6.0},
    "Mariana": {"nota1": 7.0, "nota2": 7.5},
    "Nicolas": {"nota1": 5.5, "nota2": 4.0},
    "Patricia": {"nota1": 10.0, "nota2": 9.0},
    "Rafael": {"nota1": 6.0, "nota2": 8.0}
}

print(alunos["Ana"]["nota1"], alunos["Ana"]["nota2"])

alunos["Bruno"]["nota2"] = 7.5

alunos["Eduardo"] = {"nota1": 8.0, "nota2": 6.0}

medias = {}
for nome, notas in alunos.items():
    medias[nome] = (notas["nota1"] + notas["nota2"]) / 2

for nome, media in medias.items():
    print(f"{nome}: {media:.2f}")

for nome, media in medias.items():
    if media >= 7.0:
        print(f"{nome}: {media:.2f}")

melhor_aluno = ""
maior_media = 0
for nome, media in medias.items():
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
print(f"Maior média: {melhor_aluno} com {maior_media:.2f}")

soma = 0
for media in medias.values():
    soma += media
media_geral = soma / len(medias)
print(f"Média geral da turma: {media_geral:.2f}")