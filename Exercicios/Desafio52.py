num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1   
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')        






















'''n = int(input('Digite um número: '))

if n <= 1:
    print(f'{n} não é primo.')
else:
    for c in range(2, n):
        if n % c == 0:
            print(f'{n} não é primo.')
            break
    else:
        print(f'{n} é primo.')'''


