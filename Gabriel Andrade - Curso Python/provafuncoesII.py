numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

# Função filter() para obter uma nova lista com números pares da lista numeros

# Função reduce()  para obter a soma de todos os números da lista numeros



##### FUNCAO MAP #########
def exponenciar(numero):
    return numero ** 2

exponenciados = map(exponenciar, numeros)

exponenciados = list(exponenciados)

print(exponenciados) 


##### FUNCAO FILTER ########
def par(numero):
    return numero % 2 == 0

pares = filter(par, numeros)

pares = list(pares)

print(pares)  


##### FUNCAO REDUCE #######
from functools import reduce

def somar(x, y):
    return x + y

produto = reduce(somar, numeros)

print(produto)