lista_de_tarefas = [{
    "nome": "lavar roupa",
    "descricao": "pegar roupa e colocar na maquina",
    "prioridade": "urgente",
    "categoria": "domestico",
    "concluida": False
},
{
    "nome": "lavar louça",
    "descricao": "pegar bucha e passar nas louças",
    "prioridade": "urgente",
    "categoria": "domestico",
    "concluida": False
},
{
    "nome": "passar pano",
    "descricao": "pegar rodo e passar no chao",
    "prioridade": "normal",
    "categoria": "domestico",
    "concluida": False
},
{
    "nome": "lavar banheiro",
    "descricao": "pegar vassoura e jogar agua e sabao no chao",
    "prioridade": "normal",
    "categoria": "domestico",
    "concluida": False
},
{
    "nome": "varrer a casa",
    "descricao": "pegar vassoura e passar no chao",
    "prioridade": "urgente",
    "categoria": "domestico",
    "concluida": False
},
{
    "nome": "lavar carro",
    "descricao": "pegar esponja, sabao e passar no carro",
    "prioridade": "baixa",
    "categoria": "automotiva",
    "concluida": False
},
{
    "nome": "pagar boleto",
    "descricao": "pegar celular, abrir banco e escanear qr code",
    "prioridade": "alta",
    "categoria": "financeira",
    "concluida": False
},
]


def adicionar_tarefas():
    nome_tarefa = input('Qual a tarefa a ser realizada: ')
    descricao_tarefa = input('Qual descricao dessa tarefa: ')
    prioridade = input('Qual prioridade dessa tarefa (baixa, normal, alta, urgente): ')
    categoria = input('Qual categoria dessa tarefa: ')
    concluida = False
    tarefa = {
        'nome': nome_tarefa,
        "descricao": descricao_tarefa,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': concluida,
    }
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    menu()


def ver_tarefas():
    for tarefa in lista_de_tarefas:
        print('Nome da tarefa: ', tarefa['nome'])
        print('Descrição: ', tarefa['descricao'])
        print('Prioridade: ', tarefa['prioridade'])
        print('Categoria: ', tarefa['categoria'])
        print('Concluida: ', tarefa['concluida'])
        print('-' * 10)
    menu()


def lista_por_categoria():
    categoria = input('Insira a categoria para listar as tarefas: ')
    encontradas = [tarefa for tarefa in lista_de_tarefas if tarefa['categoria'] == categoria]
    if encontradas:
        for tarefa in encontradas:
            print('Nome da tarefa: ', tarefa['nome'])
            print('Descrição: ', tarefa['descricao'])
            print('Prioridade: ', tarefa['prioridade'])
            print('Concluida: ', tarefa['concluida'])
            print('-' * 10)
    else:
        print("Nenhuma tarefa encontrada nesta categoria.")
    menu()


def lista_por_prioridade():
    prioridade = input('Insira a prioridade (baixa, normal, alta, urgente) para listar as tarefas: ')
    encontradas = [tarefa for tarefa in lista_de_tarefas if tarefa['prioridade'] == prioridade]
    if encontradas:
        for tarefa in encontradas:
            print('Nome da tarefa: ', tarefa['nome'])
            print('Descrição: ', tarefa['descricao'])
            print('Categoria: ', tarefa['categoria'])
            print('Concluida: ', tarefa['concluida'])
            print('-' * 10)
    else:
        print("Nenhuma tarefa encontrada com esta prioridade.")
    menu()


def marcar_como_concluida():
    nome_tarefa = input('Qual tarefa deseja marcar como concluída? Informe o nome exato: ')
    for tarefa in lista_de_tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefa['concluida'] = True
            print(f"Tarefa '{nome_tarefa}' marcada como concluída!")
        else:
            print(f"Tarefa '{nome_tarefa}' não encontrada.")
    menu()


def menu():
    print('Bem-vindo ao menu!')
    print('Escolha sua ação com os números de 1 a 6:')
    print('-' * 10)
    print('1 - Adicionar nova tarefa', '2 - Ver todas as tarefas', '3 - Marcar tarefa como concluída',
          '4 - Ver tarefas por prioridade', '5 - Ver tarefas por categoria', '6 - Sair', sep='\n')
    print('-' * 10)
    escolha = int(input('Qual ação deseja realizar? Digite o número correspondente a ela: '))
    if escolha == 1:
        adicionar_tarefas()
    elif escolha == 2:
        ver_tarefas()
    elif escolha == 3:
        marcar_como_concluida()
    elif escolha == 4:
        lista_por_prioridade()
    elif escolha == 5:
        lista_por_categoria()
    elif escolha == 6:
        print("Saindo...")
    else:
        print("Digite um número de ação válido!")
        menu()

menu()