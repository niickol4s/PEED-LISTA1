## Questão 20 - Crie um programa que leia uma lista de números do usuário 
# e exiba a lista ordenada em ordem decrescente.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

listaDecres = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    listaDecres.append(valor)

print(f'A lista em ordem decrescente: {sorted(listaDecres, reverse=True)}')
