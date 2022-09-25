from random import randint
from functions import Historico
class Funcionario():
    def __init__(self, nome, cpf, dataNasc, salario = 1200):
        self._nome = nome
        self._cpf = cpf
        self._dataNasc = dataNasc
class Cliente():
    def __init__(self, nome, cpf, dataNasc, profissao):
        self._nome = nome
        self._cpf = cpf
        self._dataNasc = dataNasc
        self._profissao = profissao
        
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