# def coeficiente_decrecente(ordem):
#     aux = 0
#     for l in range(50):
#         for c in range(l,50):
#             if ordem[l]['coeficiente acadêmico'] < ordem[c]['coeficiente acadêmico']:
#                 aux = ordem[l]
#                 ordem[l] = ordem[c]
#                 ordem[c] = aux
#     return ordem

# for aluno in coeficiente_decrecente(students):
#     print(f'Nome do aluno: {aluno["nome"]}')
#     print(f'Coeficiente acadêmico: {aluno["coeficiente acadêmico"]}\n')



 # Crie uma função que imprima a lista de nomes dos estudantes acompanhada da coeficiente acadêmico em ordem decrescente

def sort_students(students_dictionary):
    result = sorted(students_dictionary,key= lambda x: x['coeficiente acadêmico'], reverse=True)
    lista = []
    for estudante in result:
        tupla = (estudante['nome'], estudante['coeficiente acadêmico'], estudante['matrícula'])
        lista.append(tupla)
    return lista


## Crie uma função que imprima a lista dos estudantes ordenada por data de nascimento


