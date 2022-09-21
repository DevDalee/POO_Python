from criar_conta import * 
from datetime import datetime
from random import randint
class Historico:

    def __init__(self):
        self.__data_abertura = datetime.today()
        self.__transacoes = []
    
    @property
    def data_abertura(self):
        return self.__data_abertura
    
    @property
    def transacoes_c(self):
        return self.__transacoes

    def imprime_t(self):
        print(f'Data de abertura: {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes_c:
            print('-', t)

class Funcs():
    def __init__(self, numero, saldo):
        self.numero = numero
        self.historico = Historico() 
        self.saldo = saldo
    @property
    def saldoc(self):
        return self.__saldo
    
    @saldoc.setter
    def saldoc(self, valor):
        self.__saldo = valor
        
    @property
    def historico(self):
        return self.__historico
    
    def cria_conta_corrente(self, numero, historico, saldo = 0 ):
        numero = randint(1000, 10000)
        self.numeroc = numero
        
        print('-'*20)
        print('Conta Criada Com Sucesso!')
        print(f'{self.numeroc} é o número da conta!')
        return str(numero)
        
    def cria_conta_poup(self, numero, historico ,saldo = 0):
        numero = randint(100,1000)
        self.numerop = numero
        print('-'*20)
        print('Conta Criada Com Sucesso!')
        print(f'{self.numerop} é o número da conta!')
        print('-'*20)
        return str(numero)
    
    def depositar(self, valor):
        atual = 0
        if (valor > 0):
            atual = self.saldoc
            atual += valor
            self.saldoc = atual
            return True
        else:
            return False
        
    def sacar(self, valor):
        atual = 0
        if (valor <= self.saldoc and valor > 0):
            atual = self.saldoc
            atual -= valor
            self.saldoc = atual
            return True
        else:
            return False
        
    def transfere_para(self, destino, valor):
        retirou = self.sacar(valor)

        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes_c.append(f'Transferência de R${valor} - Para conta {destino.numeroc}')
            return True