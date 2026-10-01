'''
1. Leia números inteiros até que uma condição de parada seja atingida. Após, mostre-os.
'''

numsList = []

while True:
    nums = int(input('Digite números quaisquer(0 para parar): '))
    if nums == 0:
        break
    else:
        numsList.append(nums)
print('Números digitados: ', numsList)