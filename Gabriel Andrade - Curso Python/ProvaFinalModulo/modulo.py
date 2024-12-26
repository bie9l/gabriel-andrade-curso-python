alunos = {
    "1": "Gabriel"
}

def adicionar_alunos():
    nome_aluno = input('Digite o nome do aluno para ser adicionado: ')
    matricula = input('Qual o número de matricula do aluno: ')
    if matricula in alunos:
        print("Matrícula já cadastrada!")
    else:
        alunos[matricula] = nome_aluno
        print("Aluno adicionado com sucesso!")
    menu()


def ver_alunos():
    for matricula, nome in alunos.items():
        print('Número de matrícula: ', matricula)
        print('Nome do aluno: ', nome)
        print('-' * 10)
    menu()

def remover_aluno():
    matricula = input('Digite o número de matrícula do aluno para ser removido: ')
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno com essa matrícula não encontrado.")
    menu()

def atualizar_aluno():
    matricula = input('Digite o número de matrícula do aluno para atualizar: ')
    if matricula in alunos:
        novo_nome = input('Digite o novo nome do aluno: ')
        alunos[matricula] = novo_nome
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno com essa matrícula não encontrado.")
    menu()


def menu():
    print('Bem vindo ao menu! :)')
    print("Escolha sua ação com os numeros de 1 a 5:")
    print('-'*10)
    print('1 - Adicionar novo aluno', '2 - Ver alunos cadastrados', "3 - Remover aluno", "4 - Atualizar aluno", "5 - Sair do menu", sep='\n')
    print('-'*10)
    escolha = int(input('Qual ação deseja realizar ? Digite o numero correspondente a ela: '))
    if escolha == 1:
        adicionar_alunos()
    elif escolha == 2:
       ver_alunos()
    elif escolha == 3:
        remover_aluno()
    elif escolha == 4:
        atualizar_aluno()
    elif escolha == 5:
        pass
    else:
        print("Digite um numero de ação válido !")
