n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1+n2)/2

if media <= 5:
    print(f'Reprovado, sua média foi igual a {media:.1f} ')
elif media > 5 and media < 6.9:
    print(f'Recuperação, sua média foi igual a {media:.1f}')
elif media >= 7:
    print(f'Aprovado, sua média foi igual a {media:.1f}')        

