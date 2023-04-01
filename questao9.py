## Questão 9 - Crie um programa que leia uma lista de números do usuário 
# e exiba o menor número dessa lista.

tam = int(input('Insira o tamanho da lista: '))
lista = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    
menor = min(lista)

print(f'Menor valor da lista: {menor}')
