peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros:'))

imc = peso/(altura ** 2)

if imc < 16:
    print('Magreza grave')
elif imc <17: 
    print('Magreza moderada')
elif imc <18.5:
    print('Magreza leve')
elif imc < 25:
    print('Saudável')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (Mórbida)')                            

print(f'Seu indice de massa corporal é de {imc:.1f}')

