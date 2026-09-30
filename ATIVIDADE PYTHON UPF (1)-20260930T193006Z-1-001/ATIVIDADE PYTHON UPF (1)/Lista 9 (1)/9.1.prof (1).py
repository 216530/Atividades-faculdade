'''
1.Leia um texto interativamente através da linha de comando e retorna a contagem da ocorrência de cada letra do alfabeto no texto.
'''

def conta_letras(texto):
    contagem = {}
    
    for letra in texto.lower():
        
        if letra.isalpha():
            
            if letra not in contagem:
                contagem[letra] = 1
            
            else:
                contagem[letra] += 1
    
    return (contagem)
    
    
# programa principal
texto = input("Digite um texto: ")

retorno = conta_letras(texto)

print('\n Contagem de letras:')

for chave, valor in retorno.items():
    print(f'{chave} = {valor}')