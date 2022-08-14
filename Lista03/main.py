from funcoes import Conta

contas = {}

while(True):
    print("Menu")
    print('-'*20)
    print("1 - Criar Conta")
    print("2 - Listar Contas (Em produção)")
    print("3 - Sacar Valor")
    print("4 - Depositar Valor")
    print("5 - Excluir Conta")
    print("6 - Sair")
    escolha = int(input("Digite uma opção: "))
    print('-'*20)

    if escolha == 1:
        nome = str(input('Digite o nome do titular da conta: '))
        criar = Conta(nome, '')
        numero_conta = criar.criar_conta('')
        contas[numero_conta] = criar

    elif escolha == 2:
        print('-'*20)
        if (len(contas) == 0):
            print('Nenhuma conta existente!')
        else:
            criar.listaContas(contas)

    elif escolha == 3:
        print('-'*20)
        print('Contas Disponíveis: \n')
        criar.listaContas(contas)
        print('-'*20)
        saque = str(input('Número da conta que deseja realizar o saque'))
        if saque in contas:
            valor = float(input('Digite o valor: R$'))
            print('-'*20)
            contas[saque].sacar(valor)
        else:
            print('Conta Inválida')
        print('-'*20)
        
    elif escolha == 4:
        print('-'*20)
        print('Contas Disponíveis \n')
        criar.listaContas(contas)
        print('-'*20)
        num = str(input('Número da conta para depósito: ')).strip()

        if num in contas:
            valor = float(input('Dgite o Valor: R$'))
            print('-'*20)
            contas[num].depositar(valor)
        else: 
            print('Conta Inválida!')
        print('-'*20)

    elif escolha == 5:
        print('-'*20)
        print('Contas Disponíveis!')
        criar.listaContas(contas)
        print('-'*20)

        num = str(input('Número da conta que deseja excluir! '))

        if contas[num].saldo > 0:
            print('Saque o dinheiro antes de excluir ')
        else: 
            criar.excluir(num)
            print('Conta Excluída com sucesso!')
    elif escolha == 6:
        break