## Questão 6 - Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

from random import randint

tamanho = int(input('Insira o tamanho da lista: '))
lista = [tamanho]
print('\nValores gerados:\n')

soma = 0

for item in range(0, tamanho):
    item = randint(1, 100)
    print(item)
    soma += item
    
print(f'\nSoma dos valores: {soma}')
    