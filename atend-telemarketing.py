print("Bem vindo a nossa central de atendimento")

print ("Esolha a opção do setor com quem deseja entrar em contato: ")

print("""

    1 - FINANCEIRO\n
    2 - ADMINISTRATIVO\n
    3 - RECURSOS HUMANOS\n
    4 - ASSISTÊNCIA TÉCNICA
      
      """)

financeiro = 1
administrativo = 2
recursos_humanos = 3
assistencia_tecnica = 4

opcao_escolhida = int(input("Digite aqui o número da opção escolhida: "))

if opcao_escolhida == 1:
    print("Você será direcionado(a) para o setor Financeiro, aguarde...")

elif opcao_escolhida == 2:
    print("Você será direcionado(a) para o setor Administrativo, aguarde...")

elif opcao_escolhida == 3:
    print("Você será direcionado(a) para o setor de Recursos Humanos, aguarde...")

elif opcao_escolhida == 4:
    print("Você será direcionado(a) para o setor da Assistência Técnica, aguarde...")

opcao_escolhida2 = int(input(print("""Você deseja deixar um recado para o departamento ou falar com um de nossos atendentes?\n
      
      Responda 1 para deixar um recado:\n
      Responda 2 para falar com um de nossos atendentes:

      """)))

if opcao_escolhida2 == 1:
    str(input(print("Escreva aqui a sua mensagem: ")))
    print("""Obrigado pelo recado, nosso setor irá retornar no prazo de 24hrs.
          Para mais informções entre em contato com um de nossos atendentes""")
else :
    print("Por favor, em instantes você será atendido, aguarde...")