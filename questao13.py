## Questão 13 - Crie um programa que leia uma lista de palavras do usuário 
# e exiba somente as palavras que começam com a letra "a".

tam = int(input('Insira o tamanho da lista: '))
lista = [tam]

inicialA = []

for i in range(tam):
    palavra = str(input('Insira a palavra: '))
    lista.append(palavra)
    if palavra.startswith('a'):
        inicialA.append(palavra)

print(f'Palavras da lista com inicial "a": {inicialA}')
