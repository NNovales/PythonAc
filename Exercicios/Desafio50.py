soma = 0
cont = 0
for c in range(1,6+1):
    n = int(input('Digite um número:'))
    
    if n%2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')
