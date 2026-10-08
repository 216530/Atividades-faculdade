# funcao que retorna a nota de um aluno
def obtemNota(item) :
    # indica o campo que contem o dado da ordenacao
    # 0 = nome
    # 1 = nota
    return item[1] 

def main() :
    alunos = {}
    
    while True:
        nome = input("Nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break
        nota = float(input(f"Nota de {nome}: "))
        alunos[nome] = nota

    # Estatísticas
    quant = len(alunos)
    maior = max(alunos.values())
    menor = min(alunos.values())
    media = sum(alunos.values()) / quant
    
    ordenados = sorted(alunos.items(), key=obtemNota, reverse=True)
    
    print("\n===== RESULTADOS =====")
    print(f"Total de alunos: {quant}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média da turma: {media:.2f}")
    print(f"Notas ordenadas: {ordenados}")
    
    print("\nAlunos acima da média:")
    for aluno, nota in alunos.items() :
        if nota >= media :
            print (f"Aluno: {aluno} Nota: {nota}")

# funcao principal
main()
