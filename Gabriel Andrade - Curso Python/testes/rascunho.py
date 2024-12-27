produtos = {
    "1": "Gabriel"
}

def adicionar_produtos():
    nome_produto = input('Digite o nome do produto para ser adicionado: ')
    valor = input('Qual o valor do produto: ')
    quantidade = input('Qual a quantidade de produtos no estoque: ')
    if matricula in produtos:
        print("Matrícula já cadastrada!")
    else:
        produtos[matricula] = nome_produto
        print("produto adicionado com sucesso!")
    menu()


def ver_produtos():
    for matricula, nome in produtos.items():
        print('Número de matrícula: ', matricula)
        print('Nome do produto: ', nome)
        print('-' * 10)
    menu()

def remover_produto():
    nome_produto = input('Digite o número de matrícula do produto para ser removido: ')
    if nome_produto in produtos:
        del produtos[nome_produto]
        print("Produto removido com sucesso!")
    else:
        print("Produto com essa matrícula não encontrado.")
    menu()

def atualizar_produto():
    nome_produto = input('Digite o número de matrícula do produto para atualizar: ')
    if nome_produto in produtos:
        novo_nome = input('Digite o novo nome do produto: ')
        produtos[nome_produto] = novo_nome
        print("produto atualizado com sucesso!")
    else:
        print("produto com essa matrícula não encontrado.")
    menu()


def menu():
    print('Bem vindo ao menu! :)')
    print("Escolha sua ação com os numeros de 1 a 5:")
    print('-'*10)
    print('1 - Adicionar novo produto', '2 - Ver produtos cadastrados', "3 - Remover produto", "4 - Atualizar produto", "5 - Sair do menu", sep='\n')
    print('-'*10)
    escolha = int(input('Qual ação deseja realizar ? Digite o numero correspondente a ela: '))
    if escolha == 1:
        adicionar_produtos()
    elif escolha == 2:
       ver_produtos()
    elif escolha == 3:
        remover_produto()
    elif escolha == 4:
        atualizar_produto()
    elif escolha == 5:
        pass
    else:
        print("Digite um numero de ação válido !")
