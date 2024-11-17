# def soma(a,b):
#     return a + b

# def subtracao(a,b):
#     return a - b

# def multiplicacao(a,b):
#     return a * b

# def divisao(a,b):
#     return a/b

# def calculadora():
#     print('Bem vindo a calculadora')
#     print('Para escolher uma operação digite um numero entre 1 a 4')
#     print('1 - Soma', '2 - Subtracao', '3 - Multiplicacao', '4 - Divisão', sep='\n')
#     oper = int(input('Qual operação você deseja realizar? '))
#     num1 = int(input("Digite o primeiro numero: "))
#     num2 = int(input('Digite o segundo numero: '))
#     if oper == 1:
#         print(f'O resultado da soma é: {soma(num1, num2)}')
#     elif oper == 2:
#         print(f'O resultado da subtração é: {subtracao(num1, num2)}')
#     elif oper == 3:
#         print(f'O resultado da multiplicação é: {multiplicacao(num1, num2)}')
#     elif oper == 4:
#         print(f'O resultado da divisão é: {divisao(num1, num2)}')
#     else:
#         print("Digite um numero de operador válido")


# calculadora()


# def soma_tudo(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result


# print(soma_tudo(2, 5, 6, 9, 415, 100, 23))


# def mostrar_info(**kwargs):
#     for chave, valor in kwargs:
#         print(f'{chave}: {valor}')

# # mostrar_info(nome='João', idade='30', altura='180')


# def concatenar(*args):
#     result = ''
#     for letra in args:
#         result += letra
#     return result

# print(concatenar('b', 'a', 'n', 'a', 'n', 'a'))

# EXEMPLO FILTER:

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = list(filter(myFunc, ages))

# print(adults)


# 1 -Crie uma função que dado um valor, calcule a fatorial desse valor. 
# Ex: 3 o resultado seria 3*2*1, no caso 6;

from functools import reduce

# def calcular_fatorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado

# numero = int(input('Digite o numero que deseja fatorar'))
# resultado = calcular_fatorial(numero)
# print("O fatorial de", numero, "é", resultado)



# 2 - Crie uma função que recebe um número variável de nomes de amigos e cria uma lista com esses nomes e imprima essa lista. 


amigos = []


for amigo in range(amigos):
    amigos.append(amigo)
    print(amigos)


# 3 - Crie uma função que aceita uma lista de números e use
# a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada.



# 4 - Crie uma função que aceita uma lista de números e use
# a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.



# 5 - Crie uma função que aceita uma lista de strings e use a
# função reduce (importada de functools) para encontrar a maior string na lista.
produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro", "amoreira", "azulejo"]


def maiorstring(a, b):
    if len(a) > len(b):
        return a
    else:
        return b
    
somatorio = reduce(soma, numeros)
print(somatorio)

