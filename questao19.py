## Questão 19 - Crie um programa que leia uma lista de números do usuário 
# e exiba a lista ordenada em ordem crescente.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

listaCresc = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    listaCresc.append(valor)

print(f'A lista em ordem crescente: {sorted(listaCresc)}')
