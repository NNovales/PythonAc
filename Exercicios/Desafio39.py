from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Qual seu sexo, Masculino ou Feminino? ')).lower()
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

while sexo == 'masculino':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento')
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        ano = atual - saldo
        print(f'seu alistamento foi em {ano}')
else:
    print('Você não precisa fazer alistamento militar obrigatório.')        
