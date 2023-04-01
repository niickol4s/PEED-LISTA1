## Questão 14 - Crie um programa que leia uma lista de números do usuário 
# e exiba somente os números maiores do que 10.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

maior_que_10 = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    if valor > 10:
        maior_que_10.append(valor)

print(f'Valores maiores que 10 na lista: {maior_que_10}')
