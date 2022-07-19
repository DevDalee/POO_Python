agenda = []
def add_nome():
    adnome = str(input("Digite o nome que deseja adicionar:"))
    agenda[adnome].append("")
def add_telefone():
    nome = str(input("De quem é esse número?"))
    if nome in agenda:
        telefone = str(input("Digite o número desejado:"))
    else:
        print("Nome não existente, deseja adicionar? (S/N)")
        escolhaa = srt(input())
        if escolhaa == S:
            nomee = str(input("Digite o nome:"))
            telefone = int(intput("Digite o número:"))
            agenda[nomee].append(telefone)
def del_telefone():
    delet  = int(input("Digite o telefone que deseja deletar:"))
    if delet in agenda:
        agenda.pop(nome, delet)
def del_nome():
    aaa = str(input("Digite o nome da pessoa que deseja excluir da agenda"))
    if aaa in agenda:
        agenda.pop(aaa)
def consultar():
    numero = str(input("Quem deseja consultar os números?"))
    if numero in agenda: 
        print(agenda[nome])
    else:
        print("Essa pessoa não está na sua agenda!")
a = 1
while a > 0:
    print("Digite o número do que deseja acessar: 1 - Incluir um novo nome, 2 - Incluir um telefone, 3 - Exclur um telefone, 4 - Excluir um nome ou -1 - Para sair!")
    a = int(input())
    if a == 1:
        add_nome()
    elif a == 2:
        add_telefone()
    elif a == 3:
        del_telefone()
    elif a == 4:
        del_nome()
    elif a == 5:
        consultar()
    elif a < 0:
        break