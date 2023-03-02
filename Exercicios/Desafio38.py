first = int(input('Digite um número inteiro: '))
second = int(input('Digite outro número inteiro: '))

if first > second:
    print(f'O primeiro valor {first} é maior que o segundo valor {second}')
elif first < second: 
    print(f'O segundo valor {second} é maior que o primeiro valor {first}')
else:
    print('Não existe valor maior, os dois são iguais')
        