# lista = [0, 'Natalia', True, [0,1,2]]

# tupla = (97, 'Vinicius', 17)

# # tupla[1] = 'Rogerio'

# lista[0] = False

# print(lista)
# # print(tupla)



# Listas:

# # 1: Crie um algoritmo que, ao declararmos uma lista com o nome de três amigos, imprima:
# # o nome do primeiro amigo
# # o nome do segundo amigo
# # o nome do terceiro amigo
# #utilizando ferramenta de repeticao

# amigos = ['Miguel', 'Gabriel', 'Carlos']

# for nome in amigos:
#     print(nome)

# # print(amigos[0])
# # print(amigos[1])
# # print(amigos[2])



# 2: Dada a seguinte lista:
# animais = ["foca", "golfinho", "leão", "tartaruga"]
# Crie um algoritmo que imprima o primero e o último item da lista.

# animais = ["foca", "golfinho", "leão", "tartaruga"]

# print(animais[0])
# print(animais[-1])


# Crie um algoritmo que dado um número, imprime uma lista que contém daquele número, até 0, em ordem decrescente.
# Ex: 10,  lista_final = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10] 

# alvo = 10
# nossa_lista = []


# for numero in range(alvo+1):
#     nossa_lista.append(numero)
#     print(nossa_lista)



# 5: Dada a seguinte lista:
# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
# Crie um algoritmo que ao receber essa lista imprima os itens que iniciam com a letra "a"


# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]

# produtos_com_a = []


# for com_a in produtos:
#     if com_a[0] in ['a']:
#         produtos_com_a.append(com_a)  
#         print(produtos_com_a)



# 9: Dada duas listas:
# nomes = ["Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"]
# sobrenomes = ["Silva", "Oliveira", "Rocha", "Marques", "Amaral"]
# Crie um algoritmo que construa uma tupla com os valores nome + sobrenome correspondentes;
# Essas listas são correspondentes, então a primeira pessoa é "Bruna" e seu sobrenome é "Silva".




nomes = ["Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"]
sobrenomes = ["Silva", "Oliveira", "Rocha", "Marques", "Amaral"]
i = 0
juncao = []

for nome in nomes range (i+1):
    print(nomes[i], sobrenomes[i])












#     bruna.append(nome[0])  
#     print(bruna)


# print




# for nome in nomes:
#         juncao.append(nome)  
#         print(juncao)

# for sobrenome in sobrenomes:
#         juncao.append(sobrenome)  
#         print(juncao)

# for i in nomes + sobrenomes:
#         juncao.append(i)
#         print(juncao)


# print(f'{nomes[0]} {sobrenomes[0]}')
# print(f'{nomes[1]} {sobrenomes[1]}')
# print(f'{nomes[2]} {sobrenomes[2]}')
# print(f'{nomes[3]} {sobrenomes[3]}')
# print(f'{nomes[4]} {sobrenomes[4]}')