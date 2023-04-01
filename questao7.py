## Questão 7 - Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

maior = ''

for item in range(tam):
    palavra = str(input('Insira a palavra: '))
    lista.append(palavra)
    if len(palavra) > len(maior):
        maior = palavra

print(f'Maior palavra da lista: "{maior}".')
