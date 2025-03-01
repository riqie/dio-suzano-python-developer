# ======== FUNÇÕES DE USUÁRIO ==========
def cadastrarUsuario(lista_usuarios):
    nome = input('Informe o nome do usuário: ')
    cpf = input('Informe o CPF do usuário: ')

    if verificarUsuario(lista_usuarios, cpf):
        print('Usuário já cadastrado.')
        return 

    data_nascimento = input('Informe a data de nascimento do usuário: ')
    endereco = input('Informe o endereço do usuário: ')

    usuario = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }

    lista_usuarios.append(usuario)
    print(f'Usuário {nome} cadastrado com sucesso!')


def verificarUsuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            return usuario  
    return None


# ======== FUNÇÕES DE CONTA BANCÁRIA ==========
def criarContaBancaria(lista_contas, AGENCIA, lista_usuarios):
    cpf_usuario = input('Informe o CPF do usuário para criar a conta: ')

    # Verificar se o CPF existe na lista de usuários
    usuario = verificarUsuario(lista_usuarios, cpf_usuario)
    if usuario is None:
        print("CPF não encontrado. Não é possível criar a conta.")
        return

    agencia = AGENCIA
    numero = input('Informe o número da conta: ')
    banco = input('Informe o banco: ')

    conta = {
        'agencia': agencia,
        'numero': numero,
        'banco': banco
    }

    lista_contas.append(conta)  
    print(f'Conta {numero} criada com sucesso!')


# ======== FUNÇÕES DE TRANSAÇÕES ==========
def realizarDeposito(saldo, extrato, lista_contas):
    print("\nDepósito.")
    numero_conta = input("Informe o número da conta: ")

    valor = registrar_valor()

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        valor_invalido()

    return saldo, extrato


def realizarSaque(saldo, limite, extrato, n_saques, LIMITE_SAQUES, lista_contas):
    print("\nSaque.")
    numero_conta = input("Informe o número da conta: ")

    valor = registrar_valor()

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = n_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        saldo_insuficiente()
    elif excedeu_limite:
        print("\nO valor do saque excede o limite permitido.")
    elif excedeu_saque:
        print("\nNúmero máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        n_saques += 1
        print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
    else:
        valor_invalido()

    return saldo, extrato, n_saques


def exibirExtrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if not extrato:
        print('Nenhuma movimentação registrada.')
    else:
        print(extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')

    return saldo, extrato


# ======== FUNÇÕES AUXILIARES ==========
def sair():
    print("\nSaindo...")


def opcao_invalida():
    print('\nOpção inválida.')


def valor_invalido():
    print('Operação falhou devido ao valor inválido informado.')


def menu():
    print('\n\n -- Conta Bancária -- \nEscolha uma das opções abaixo:')
    print('[1] - Novo Usuário\n[2] - Nova Conta\n[3] - Depositar\n[4] - Sacar\n[5] - Extrato\n[6] - Listar Contas\n[7] - Sair')


def saldo_insuficiente():  
    print('\nVocê não possui saldo suficiente.')


def registrar_valor():
    try:
        valor = float(input('Informe o valor: R$ '))
        return valor
    except ValueError:
        print("Valor inválido. Insira um número válido.")
        return 0


# ======== NOVO MÉTODO ==========
def listarContas(lista_contas):
    if not lista_contas:
        print("\nNenhuma conta registrada.")
    else:
        print("\n===== LISTA DE CONTAS =====")
        for conta in lista_contas:
            print(f'Agência: {conta["agencia"]} | Número: {conta["numero"]} | Banco: {conta["banco"]}')


# ======== FUNÇÃO PRINCIPAL ==========
def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ''
    n_saques = 0
    lista_usuarios = []
    lista_contas = []

    while True:
        menu()
        opcao = input("\n :")

        if opcao == '1':
            cadastrarUsuario(lista_usuarios)

        elif opcao == '2':
            criarContaBancaria(lista_contas, AGENCIA, lista_usuarios)

        elif opcao == '3':
            saldo, extrato = realizarDeposito(saldo, extrato, lista_contas)

        elif opcao == '4':
            saldo, extrato, n_saques = realizarSaque(saldo, limite, extrato, n_saques, LIMITE_SAQUES, lista_contas)

        elif opcao == '5':
            saldo, extrato = exibirExtrato(saldo, extrato)

        elif opcao == '6':
            listarContas(lista_contas)

        elif opcao == '7':
            sair()
            break

        else: 
            opcao_invalida()
            continue


main()
