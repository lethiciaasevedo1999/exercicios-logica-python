numero_secreto = 5

print("Tente adivinhar o número secreto, vamos lá ! ")
tentativa = int(input("Digite um número de 1 a 100: "))

if tentativa == numero_secreto:
    print("Parabéns você acertou o número secreto !!!")
elif tentativa < numero_secreto:
    print("Que pena, você chutou baixo :( ...)")
    
else :
    print("Eita, você chutou alto '-'")