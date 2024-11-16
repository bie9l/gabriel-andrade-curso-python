alunos = []

def adicionar_aluno():
    nome_aluno = input('Digite o nome do aluno: ')
    numero_matricula = input('Digite o numero da matricula: ')
    dados = {
        'nome': nome_aluno,
        "matricula": numero_matricula,
    }
    alunos.append(dados)
    menu()

def ver_alunos():
    for dados in alunos:
        print('Nome do aluno: ', dados['nome'])
        print('Matricula: ', dados['matricula'])
        print('-'*10)
    menu()

def remover_alunos():
    print('Alunos:', alunos)
    num_matricula = input('Digite o número da matrícula do aluno que você deseja remover: ')
    for dados in alunos:
        if dados['matricula'] == num_matricula:
            alunos.remove(dados)
            print('Aluno removido com sucesso!')
            break
    else:
        print('Aluno não encontrado com o número de matrícula fornecido.')
    menu()

def menu():
    print('Bem vindo ao menu!: ')
    print("Escolha sua ação com os numeros de 1 a 3:")
    print('-'*10)
    print('1 - Adicionar novo aluno', '2 - Ver todos os alunos', "3 - Remover aluno", "4 - Sair", sep='\n')
    print('-'*10)
    escolha = int(input('Qual ação deseja realizar ? Digite o numero correspondente a ela: '))
    if escolha == 1:
        adicionar_aluno()
    elif escolha == 2:
       ver_alunos()
    elif escolha == 3:
        remover_alunos()
        

    elif escolha == 4:
        pass
    else:
        print("Digite um numero de ação válido !")

menu()


    
# def remover_alunos():
#     print(f'Qual o numero da matricula do aluno que você deseja remover ? \n {alunos}')
#     num_matricula = input('Digite o numero da matricula: ')
#     for dados in alunos:
#         if dados['matricula'] == num_matricula:
#             remove(alunos.index(''))
#         print('-'*10)
#     menu()
