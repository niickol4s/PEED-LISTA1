## Questão 10 - Crie um programa que leia uma lista de números do usuário e exiba a média desses números.

tam = int(input('Insira o tamanho da lista: '))
lista = []

for i in range(tam):
    valor = int(input(f'Insira o {i + 1}º valor: '))
    lista.append(valor)
    
soma = sum(lista)
media = soma / len(lista)

print(f'Valores inseridos: {lista}')
print(f'Soma dos valores: {soma}')
print(f'Média dos valores: {media:.2f}')
