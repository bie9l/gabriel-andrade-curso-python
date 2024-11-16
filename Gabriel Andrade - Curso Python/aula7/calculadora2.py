# EXERCICIO: crie um arquivo calculadora.py , este arquivo deve executar apenas a função de menu da calculadora onde o usuário escolhe sua operação, 
# as funções auxiliares (soma, subtração, etc..., devem ser colocadas em um arquivo a parte e importadas como módulo


from calculatorAuxiliary import *

def calculadora():
    print('Bem vindo a calculadora')
    print('Para escolher uma operação digite um numero entre 1 a 4')
    print('1 - Soma', '2 - Subtracao', '3 - Multiplicacao', '4 - Divisão', sep='\n')
    oper = int(input('Qual operação você deseja realizar? '))
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input('Digite o segundo numero: '))
    if oper == 1:
        print(f'O resultado da soma é: {soma(num1, num2)}')
    elif oper == 2:
        print(f'O resultado da subtração é: {subtracao(num1, num2)}')
    elif oper == 3:
        print(f'O resultado da multiplicação é: {multiplicacao(num1, num2)}')
    elif oper == 4:
        print(f'O resultado da divisão é: {divisao(num1, num2)}')
    else:
        print("Digite um numero de operador válido")


calculadora()

