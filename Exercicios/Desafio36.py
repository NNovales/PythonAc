valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
meses = tempo*12 
prestacao = valorcasa/meses
teto = salario*(30/100)

if prestacao > teto:
    resposta = input(f'Para pagar uma casa de R${valorcasa} em {tempo} anos a prestação será de R${prestacao:.2f} Empréstimo NEGADO!')
else:
    print(f'Parabéns!, seu limite foi aprovado, sua casa no valor de {valorcasa} será totalmente quitada depois de {tempo} anos ou {meses} meses com parcelas no valor de R${prestacao:.2f}')




