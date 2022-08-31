from funcoes import Func
import datetime

nome = str(input('Digite o Nome: '))
Ano_nasci = int(input('Digite a Data de Nascimento: '))
Altura = float(input('Digite a Altura: '))

Pessoa = Func(nome,Ano_nasci,Altura)
for x in range(len(Pessoa)):
    print(Pessoa)
