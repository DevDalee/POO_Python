class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def armazenar(self, nome):
        self.nome = nome
        print('-' * 30)
        print('Pessoa Aramazenada!')
        print('-' * 30)
        return str(nome)

    def listar_agenda(self, agenda):
        for nome in agenda.items():
            print(self.nome)
