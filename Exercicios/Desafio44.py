print(' LOJA SIMPLES '.center(40, '='))
preco = float(input('Preço das compras: R$ '))
pagamento = int(input('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a forma de pagamento? '''))

if pagamento == 1:
    print(f"Você teve um desconto de 10% e o seu produto saiu por apenas R$ {preco - preco*0.10:.2f}")
elif pagamento == 2:
     print(f"Você teve um desconto de 5% e o seu produto saiu por apenas R$ {preco - preco*0.05:.2f}")
elif pagamento == 3:
    print(f"Sua compra será parcelada em 2x de R${preco/2:.2f}")
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'''Sua compra será parcelada em {parcelas}x de R${(preco/parcelas) + (preco*0.2)/parcelas:.2f} COM JUROS de 20%
    Sua compra de R${preco:.2f} vai custar R${preco + preco*0.20:.2f} no final.''')
else:
    total = 0
    print(f'''OPÇÃO INVÁLIDA de pagamento. Tente novamente!
    Sua compra de R${preco:.2f} vai custar R${preco:.2f} no final.''')    



   







'''preco = float(input('Valor do produto: '))
pagamento = input('Qual a forma de pagamento: ')

if pagamento == 'a vista':
    desconto = preco * 0.10
    preco_final = preco - desconto
    print("Você teve um desconto de 10% e o seu produto saiu por apenas R$", preco_final)
elif pagamento == 'debito':
    desconto = preco * 0.05
    preco_final = preco - desconto
    print("Você teve um desconto de 5% e o seu produto saiu por apenas R$", preco_final)
elif pagamento == '2x':
    print("O seu produto saiu por apenas R$", preco)
elif pagamento == '3x':
    juros = preco * 0.20
    preco_final = preco + juros
    print("Você teve um acréscimo de 20% de juros seu produto saiu por apenas R$", preco_final)'''

