frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) 
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')        















'''def is_palindrome(sentence):
    # Remover espaços e pontuação
    sentence = sentence.lower().replace(" ", "").replace(",", "").replace(".", "")
    # Inverter a frase
    reverse = sentence[::-1]
    # Verificar se a frase invertida é igual à original
    return sentence == reverse

sentence = input("Digite uma frase: ")
if is_palindrome(sentence):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")'''
