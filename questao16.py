## Questão 16 - Crie um programa que leia uma lista de números do usuário 
# e exiba a soma dos números pares.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

par = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
        soma = sum(par)

print(f'Valores pares da lista: {par}')
print(f'Soma dos valores pares da lista: {soma}')