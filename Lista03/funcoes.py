
class Conta:

    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            return f'Saque Realizado Com Sucesso'
        else:
            return f'Operação não realizada'
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

    def listar(self):
        print("Titular da conta: {} \n Numero: {} \nSaldo: {:.2f}".format(self.titular, self.numero, self.saldo))	
    