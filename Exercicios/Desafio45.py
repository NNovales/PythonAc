import random
from time import sleep
print("Bem-Vindo ao jogo de Pedra, Papel ou Tesoura!")

#Lista de escolhas
escolhas = ["pedra", "papel", "tesoura"]

#Escolha do usuario
usuario_escolha = input('''por favor escolha uma das opções:
PEDRA
PAPEL
TESOURA

''').lower()
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
print('-=' * 23)

#Verificação de validade de escolha
while usuario_escolha not in escolhas:
    print("Escolha invalida, por favor escolha uma opção valida.")
    usuario_escolha = input("por favor escolha uma das opções: pedra, papel, tesoura").lower()

#Escolha do computador
computador_escolha = random.choice(escolhas)

#Comparação das escolhas e definição do vencedor
if usuario_escolha == computador_escolha:
    print(f"Isso é um empate! vocês dois escolheram {usuario_escolha}")
elif usuario_escolha == "pedra" and computador_escolha == "tesoura":
    print("Você venceu! pedra vence tesoura.")
elif usuario_escolha == "papel" and computador_escolha == "pedra":
    print("Você venceu! papel vence pedra.")
elif usuario_escolha == "tesoura" and computador_escolha == "papel":
    print("Você venceu! tesoura vence papel.")
else:
    print("Você perdeu! O computador escolheu", computador_escolha)                
print('-='*23)
