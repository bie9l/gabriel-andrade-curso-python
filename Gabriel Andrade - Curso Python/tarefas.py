from functools import reduce


tarefa1 = [ {
    "nome":"lavar roupa",
    "descricao":"pegar roupa, e colocar na maquina",
    "prioridade":"urgente",
    "categoria":"domestico",
    "concluida": False
},
{
    "nome":"lavar louça",
    "descricao":"pegar bucha, e passar nas louças",
    "prioridade":"urgente",
    "categoria":"domestico",
    "concluida": False
},
{
    "nome":"passar pano",
    "descricao":"pegar rodo, e passar no chao",
    "prioridade":"normal",
    "categoria":"domestico",
    "concluida": False
},
{
    "nome":"lavar banheiro",
    "descricao":"pegar vassoura, e jogar agua e sabao no chao",
    "prioridade":"normal",
    "categoria":"domestico",
    "concluida": False
},
{
    "nome":"varrer a casa",
    "descricao":"pegar vassoura, e passar no chao",
    "prioridade":"urgente",
    "categoria":"domestico",
    "concluida": False
},
{
    "nome":"lavar carro",
    "descricao":"pegar esponja, sabao e passar no carro",
    "prioridade":"baixa",
    "categoria":"automotiva",
    "concluida": False
},
{
    "nome":"pagar boleto",
    "descricao":"pegar celular, abrir banco e escanear qr code",
    "prioridade":"alta",
    "categoria":"financeira",
    "concluida": False
},
]

def adicionar_tarefas():
    nome_tarefa = input('Qual a tarefa a ser realizada: ')
    categoria = input('Qual categoria dessa tarefa: ')
    concluida = False
    prioridade = input('Qual prioridade dessa tarefa: ')
    descricao_tarefa = input('Qual descricao dessa tarefa: ')
    tarefa = {
        'nome': nome_tarefa,
        "descricao": descricao_tarefa,
        'categoria': categoria,
        "prioridade": prioridade,
        'concluida': concluida,
    }
    tarefa1.append(tarefa)
    menu()



def ver_tarefas():
    for tarefa in tarefa1:
        print('Nome da tarefa: ', tarefa['nome'])
        print('Descrição: ', tarefa['descricao'])
        print('Categoria: ', tarefa['categoria'])
        print('Prioridade: ', tarefa['prioridade'])
        print('Concluida: ', tarefa['concluida'])
        print('-'*10)
    menu()




def listaCategoria(tarefa1):
    lista = []
    for i in tarefa1:
        categoria = i['categoria']
        if categoria  == 'domestico':
            lista.append(i)
    return lista


# def listaPrioridade(tarefa1):
#     if prioridade == 'urgente'


# result = sorted(students_dictionary,key= lambda x: x['coeficiente acadêmico'], reverse=True)

# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro", "amoreira", "azulejo"]


# def maiorstring(a, b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b
    
# somatorio = reduce(soma, numeros)
# print(somatorio)




def menu():
    print('Bem vindo ao menu! :)')
    print("Escolha sua ação com os numeros de 1 a 6:")
    print('-'*10)
    print('1 - Adicionar nova tarefa', '2 - Ver todas tarefas', "3 - Marcar tarefa como concluida", "4 - Ver tarefas por prioridade", "5 - Ver tarefas por categoria", sep='\n')
    print('-'*10)
    escolha = int(input('Qual ação deseja realizar ? Digite o numero correspondente a ela: '))
    if escolha == 1:
        adicionar_tarefas()
    elif escolha == 2:
       ver_tarefas()
    elif escolha == 3:
        print(f'Qual tarefa deseja marcar como concluida ? \n {tarefa1}')
        #numero tarefa, e de acordo com o numero, concluida = True
    elif escolha == 4:
        listaCategoria()
        pass
        #fazer def listando as tarefas por categoria e printar
    elif escolha == 5:
        # listaPrioridade()
        pass
        #fazer def listando as tarefas por prioridade e printar
    elif escolha == 6:
        pass
    else:
        print("Digite um numero de ação válido !")


menu()



# menu:
# bem vindo a lista de tarefa, escolha o que deseja fazer

# 1 - adicionar nova tarefa
# 2 - ver todas as tarefas
# 3 - marcar como concluida uma tarefa 
# 4 - classifcar tarefas por prioridade
# 5 - classifcar tarefas por categoria
# 6 - sair

