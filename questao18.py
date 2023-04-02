## Questão 18 - Crie um programa que leia uma lista de números do usuário 
# e exiba o produto desses números.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

mult = 1

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    mult *= valor

print(f'Produto dos valores da lista: {mult}')
