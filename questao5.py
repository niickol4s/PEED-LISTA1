## Questão 5 - Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.

number = int(input('Insira um número: '))

if number % 2 == 0:
    print(f'{number} é par.')
else:
    print(f'{number} é ímpar.')
    