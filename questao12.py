## Questão 12 - Crie um programa que leia uma lista de números do usuário 
# e exiba somente os números ímpares.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

impar = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    if valor % 2 != 0:
        impar.append(valor)

print(f'Valores ímpares da lista: {impar}')
