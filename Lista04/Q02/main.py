from pessoa import Pessoa

agenda = {}

def listar():
    print('-' * 30)
    print('Nomes na Agenda: \n')
    c.listar_agenda(agenda)
    print('-' * 30)

while True:
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print('[1] - Armazenar Pessoa')
    print('[2] - Remover Pessoa')
    print('[3] - Buscar Pessoa')
    print('[4] - Imprimir Agenda')
    print('[0] - Sair')
    print('-' * 30)
    resp = int(input('Digite sua opção: '))

    if (resp == 0):

        break

    elif (resp == 1):

       nome = str(input('Digite o nome que deseja armazenar: ')).strip()
       c = Pessoa(nome)
       nomes = c.armazenar(nome)

       if nomes not in agenda:
        agenda[nome] = c
       else:
        while nomes in agenda:
                nomes = c.armazenar(nome)
        agenda[nome] = c

    elif (resp == 2):
        
        listar()
        nomex = str(input('Digite o nome que deseja excluir: ')).strip()
        print('-' * 30)
        if agenda[nomex] in agenda.items():
            agenda.pop(nomex)
            print('Nome removido com sucesso!')
        else:
            print('Erro ao remover esse nome')
        print('-'*30)

    elif (resp == 3):

        print('-'*30)
        busca = str(input('Digite o nome que deseja buscar: '))
        if(len(agenda) == 0):
            print("Nenhum nome na agenda")
        else: 
            c.listar_agenda(agenda), print('Está na Agenda')

    elif (resp == 4):
        listar()