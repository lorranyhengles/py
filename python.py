nome= input('digite seu nome:')
salario= int(input('digite seu salario:'))
valor_emprestimo= int(input('digite o valor do emprestimo:'))
if (salario <1000) or (valor_emprestimo <2000) or (valor_emprestimo > salario*15) :
    print ('negado',nome)
else :
    print ('aprovado',nome)
    