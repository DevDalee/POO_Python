from funcoes import Conta

contas = {}

c = Conta('Marcos', '123')
c1 = Conta('Arthur', '321', 1000000000000)
c2 = Conta('Mayra', '213', 6)
c3 = Conta('Luiz Nelson', '888', 45)
c4 = Conta('Miss', '777', 30)

for chave, valor in contas.items():
    valor.listar()


'''
while(True):
    print("1 - Criar Conta")
    print("2 - Listar Contas (Em produção)")
    print("3 - Sacar Valor")
    print("4 - Depositar Valor")
    print("5 - Excluir Conta")
    print("6 - Sair")
    escolha = int(input("Digite uma opção: "))
'''