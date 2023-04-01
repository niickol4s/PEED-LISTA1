## Questão 15 - Crie um programa que leia uma lista de números do usuário 
# e exiba somente os números menores do que 5.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

menor_que_5 = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    if valor < 5:
        menor_que_5.append(valor)

print(f'Valores menores que 5 na lista: {menor_que_5}')