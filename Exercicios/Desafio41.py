from datetime import date 
atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento


if idade <= 9:
    print(f'De acordo com a sua idade {idade} anos, você se enquadra na categoria MIRIM')
elif idade <= 14:
    print(f'De acordo com a sua idade {idade} anos, você se enquadra na categoria INFANTIL')
elif idade <= 19:
    print(f'De acordo com a sua idade {idade} anos, você se enquadra na categoria JUNIOR')
elif idade <= 25:
    print(f'De acordo com a sua idade {idade} anos, você se enquadra na categoria SêNIOR')
else:
    print(f'De acordo com a sua idade {idade} anos, você se enquadra na categoria MASTER')
                     
