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