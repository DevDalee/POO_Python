import datetime

class Func:
    def __init__(self, nome, nascimento, altura):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__altura = altura

    def calcIdade(self):
        current_date = datetime.date.today()
        data_actual = current_date.year
        idade = data_actual-self.nascimento
        return idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura