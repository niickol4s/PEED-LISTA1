## Questão 11 - Crie um programa que leia uma lista de números do usuário 
# e exiba somente os números pares.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

par = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)

print(f'Valores pares na lista: {par}')
