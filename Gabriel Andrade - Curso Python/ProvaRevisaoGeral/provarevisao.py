produtos = []
totalProdutos = 0.0

def adicionar_produtos():
    global totalProdutos
    nome_produto = input('Digite o nome do produto para ser adicionado: ')
    valor = float(input('Qual o valor unitário do produto: '))
    quantidade = int(input('Qual a quantidade de produtos no estoque: '))
    for produto in produtos:
        if produto['nome'] == nome_produto:
            print("Produto já cadastrado!")
            return menu()
    
    total = valor * quantidade
    totalProdutos += total
    
    produtos.append({"nome": nome_produto, "valor": valor, "quantidade": quantidade, "total": total})
    print("Produto adicionado com sucesso!")
    menu()

def ver_produtos():
    global totalProdutos
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f'Nome do produto: {produto["nome"]}')
            print(f'Valor unitário: {produto["valor"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print(f'Valor total do produto: {produto["total"]}')
            print('-' * 10)
        print(f'Valor total de todos os produtos: {totalProdutos}')
    menu()

def remover_produto():
    global totalProdutos
    nome_produto = input('Digite o nome do produto para ser removido: ')
    for produto in produtos:
        if produto['nome'] == nome_produto:
            totalProdutos -= produto['total']
            produtos.remove(produto)
            print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")
    menu()

def atualizar_produto():
    global totalProdutos
    nome_produto = input('Digite o nome do produto para atualizar: ')
    for produto in produtos:
        if produto['nome'] == nome_produto:
            totalProdutos -= produto['total']
            novo_nome = input('Digite o novo nome do produto: ')
            novo_valor = float(input('Digite o novo valor unitário do produto: '))
            nova_quantidade = int(input('Digite a nova quantidade do produto: '))
            novo_total = novo_valor * nova_quantidade
            produto.update({"nome": novo_nome, "valor": novo_valor, "quantidade": nova_quantidade, "total": novo_total})
            totalProdutos += novo_total
            print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")
    menu()

def menu():
    print('Bem-vindo ao menu! :)')
    print("Escolha sua ação com os números de 1 a 5:")
    print('-'*10)
    print('1 - Adicionar novo produto')
    print('2 - Ver produtos cadastrados')
    print('3 - Remover produto')
    print('4 - Atualizar produto')
    print('5 - Sair do menu')
    print('-'*10)
    escolha = int(input('Qual ação deseja realizar? Digite o número correspondente a ela: '))
    if escolha == 1:
        adicionar_produtos()
    elif escolha == 2:
        ver_produtos()
    elif escolha == 3:
        remover_produto()
    elif escolha == 4:
        atualizar_produto()
    elif escolha == 5:
        print("Encerrando.")
    else:
        print("Digite um número de ação válido!")
        menu()

menu()