import random

# Função para criar um usuário
def criar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF (somente números): ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    
    # Verifica se o CPF já está cadastrado
    if cpf in usuarios:
        print("Erro! Já existe um usuário cadastrado com este CPF.")
        return None
    
    # Cria um novo usuário
    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "contas": []  # Lista para armazenar as contas do usuário
    }
    
    print(f"Usuário {nome} criado com sucesso!")
    return cpf

# Função para criar uma conta corrente vinculada ao usuário
def criar_conta_corrente(usuarios, cpf):
    if cpf not in usuarios:
        print("Erro! CPF não encontrado. Por favor, crie um usuário antes de criar uma conta.")
        return None
    
    numero_conta = random.randint(10000, 99999)  # Gerar número de conta aleatório
    conta = {
        "numero": numero_conta,
        "saldo": 0,  # Saldo inicial
        "historico": []  # Histórico de movimentações
    }
    
    usuarios[cpf]['contas'].append(conta)
    print(f"Conta número {numero_conta} criada com sucesso!")
    return numero_conta

# Funções de depósito, saque e extrato (mesmas da versão anterior)
def exibir_menu():
    print("\nO que você gostaria de fazer?")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Ver extrato")
    print("4- Encerrar")
    return input("Escolha uma opção: ")

def depositar(conta):
    try:
        valor = float(input("Quanto você quer depositar? "))
        if valor > 0:
            conta['saldo'] += valor
            conta['historico'].append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro! Valor de depósito inválido.")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def sacar(conta):
    try:
        valor = float(input("Quanto você gostaria de sacar? (Limite de R$500) "))
        if valor > conta['saldo']:
            print("Erro! Saldo insuficiente.")
        elif valor > 500:
            print("Erro! Seu limite é de R$500.")
        elif valor <= 0:
            print("Erro! Valor de saque inválido.")
        else:
            conta['saldo'] -= valor
            conta['historico'].append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Erro! Por favor, insira um valor numérico válido.")

def exibir_extrato(conta):
    if not conta['historico']:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        print("\nExtrato de movimentações:")
        for transacao in conta['historico']:
            print(transacao)
    print(f"Saldo atual: R${conta['saldo']:.2f}\n")

# Programa principal
usuarios = {}

while True:
    print("\n=== Bem-vindo ao Banco X ===")
    print("1- Criar usuário")
    print("2- Criar conta corrente")
    print("3- Acessar conta")
    print("4- Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        criar_usuario(usuarios)
    
    elif opcao == '2':
        cpf = input("Digite o CPF do usuário para vincular a conta: ")
        criar_conta_corrente(usuarios, cpf)

    elif opcao == '3':
        cpf = input("Digite o CPF do usuário: ")
        
        if cpf not in usuarios or not usuarios[cpf]['contas']:
            print("Erro! Usuário não encontrado ou sem contas cadastradas.")
        else:
            print(f"Usuário encontrado: {usuarios[cpf]['nome']}")
            for i, conta in enumerate(usuarios[cpf]['contas']):
                print(f"Conta {i + 1}: Número {conta['numero']}, Saldo: R${conta['saldo']:.2f}")
            
            numero_conta = int(input("Digite o número da conta que deseja acessar: "))
            conta_atual = next((conta for conta in usuarios[cpf]['contas'] if conta['numero'] == numero_conta), None)
            
            if conta_atual:
                while True:
                    escolha = exibir_menu()
                    if escolha == '1':
                        depositar(conta_atual)
                    elif escolha == '2':
                        sacar(conta_atual)
                    elif escolha == '3':
                        exibir_extrato(conta_atual)
                    elif escolha == '4':
                        print("Encerrando o acesso à conta.")
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Erro! Conta não encontrada.")

    elif opcao == '4':
        print("Obrigado por usar o Banco X. Até mais!")
        break

    else:
        print("Opção inválida!")
