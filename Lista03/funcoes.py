from random import randint

class Conta:

    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def criar_conta(self, numero):
        numero = randint(100, 1000)
        self.numero = str(numero)

        print('-' * 30)
        print('Conta criada com sucesso!')
        print(f'{self.numero} é o número da conta!')
        print('-' * 30)
        return str(numero)

    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            return f'Saque Realizado Com Sucesso'
        else:
            return f'Operação não realizada'

    def extrato(self):
        print(f'Titular da conta: {self.titular.nome}')
        print(f'CPF do titular: {self.titular.cpf}')
        print(f'Número da conta: {self.numero}')
        print(f'Saldo da conta: R${self.saldo:.2f}')
        print('\n')   

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Deposito Efetuado Com Sucesso'
        else:
            return f'Operação não realizada'  

    def excluir(self, numero):
        if numero in Conta:
            Conta.pop(numero)
            return f'Operação Realizada Com Sucesso!'

    def listaContas(self, contas):
        for chave, valor in contas.items():
            valor.extrato()

    def transferir(self, destino, valor):
        operacao = self.sacar(valor)

        if operacao == False:
            return False
        else:
            destino.depositar(valor)
            return True
    