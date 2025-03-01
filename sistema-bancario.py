
def main():
    menu = '\n -- Conta Bancária -- \n\nEscolhe uma das opções abaixo: \n[1] - Depositar \n[2] - Sacar \n[3] - Extrato \n[4] - Sair\n:'

    saldo = 0
    limite = 500
    extrato = ''
    n_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = input(menu)

        if opcao == '1':
            print("\nDepósito.")
            valor = float(input('Qual o valor que deseja depositar?\n:'))

            if valor > 0:
                saldo += valor
                extrato += f'Depósito: R$ {valor:.2f}\n'

            else:
                print('Operação falhou devido ao valor inválido informado.')

        elif opcao == '2':
            print("\nSaque.")
            valor = float(input('Qual o valor que deseja sacar?\n:'))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = n_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print('\nVocê não possui saldo suficiente.')
            
            elif excedeu_limite:
                print('\nVocê não possui limite suficiente.')

            elif excedeu_saque:
                print('\nVoce não possui saques suficiente.')

            elif valor > 0:
                saldo -= valor
                extrato += f'Saque de R$ {valor:.2f}\n'
                n_saques +=1

            else:
                print('Valor inválido!')
            

        elif opcao == '3':
            print("\nExtrato.")
            print(' ===== EXTRATO =====')
            
            if not extrato:
                print('Não foram realizadas movimentações na conta!')
            
            else:
                print(f'\nSaldo: R$ {saldo:.2f}')

        elif opcao == '4':
            print("\nSaindo.")
            break

        else: 
            print('\nOpção inválida.')

main()





