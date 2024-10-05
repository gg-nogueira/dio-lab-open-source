saldo = 1000
historico = []
while (True):
  resposta = int(input(print (f"Olá! Bem vindo ao banco X\nSeu saldo é de R${saldo}\nO que você gostaria de fazer?\n1- Depositar\n2- Sacar\n3- Historico\n4- Encerrar\n")))
  if resposta == 1:
    depositar = float(input(print("Quanto você quer depositar?")))
    saldo += depositar
    historico.append(f"\nDeposito:R${depositar:.2f}\n") 
    print(saldo)

  elif resposta == 2:
    sacar = float(input(print("\nQuanto você gostaria de sacar? (Limite de R$500)\n")))
    if sacar > saldo:
      print("\nErro!! Saldo insuficiente\n")
    elif sacar > 500:
      print("\nErro!! Seu limite é de R$500\n")
    else:
      saldo -= sacar
      historico.append(f"\nSaque: -R${sacar:.2f}\n")
      print(saldo)

  elif resposta ==3:
    print("\nExtrato de movimentações:")
    print(historico)
  
  elif resposta == 4:
    print("\nObrigado! Tenha um ótimo dia!\n")
    break

  else:
    print("\nDigite uma resposta válida!\n")
