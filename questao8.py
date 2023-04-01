## Questão 8 - Crie um programa que leia uma lista de números do usuário 
# e exiba o maior número dessa lista.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)

maior = max(lista)

print(f'Maior valor da lista: {maior}')
