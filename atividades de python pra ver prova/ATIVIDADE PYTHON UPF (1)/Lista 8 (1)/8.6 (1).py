'''
6. Elaborar um função que receba um número inteiro
com argumento e retorne se o mesmo é primo ou não.
'''

def testa_primo(numero):
    # Número menor ou igual a 1 não é primo
    if numero <= 1:
        return False
        
    # Testa se ele divide por 2 até ele mesmo 
    for i in range(2, numero):
        if numero % i == 0:
            return False
            
    return True

print(testa_primo(7))   # True
print(testa_primo(4))   # False
print(testa_primo(1))   # False
print(testa_primo(-5))  # False
print(testa_primo(13))  # True