notas = []

def adicionar_notas():
    aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota: '))
    dados = {
        'nome do aluno': aluno,
        'nota': nota,
    }
    notas.append(dados)
    print("Nota adicionada com sucesso!")
    menu()

def calcular_media():
    if not notas:
        print("Nenhuma nota cadastrada.")
    else:
        soma = sum(dado['nota'] for dado in notas)
        media = soma / len(notas)
        print(f"A média das notas é: {media}")
    menu()

def verificar_situacao():
    if not notas:
        print("Nenhuma nota cadastrada.")
    else:
        soma = sum(dado['nota'] for dado in notas)
        media = soma / len(notas)
        if media < 7:
            print('Aluno reprovado')
        elif media == 10:
            print('Parabéns, sua média é 10')
        else:
            print('Aluno aprovado')
    menu()

def menu():
    print('\nBem vindo ao menu!')
    print("Escolha sua ação com os números de 1 a 4:")
    print('-' * 10)
    print('1 - Adicionar nota')
    print('2 - Gerar média')
    print("3 - Verificar situação do aluno")
    print("4 - Sair")
    print('-' * 10)

    escolha = int(input('Qual ação deseja realizar? Digite o número correspondente a ela: '))

    if escolha == 1:
        adicionar_notas()
    elif escolha == 2:
        calcular_media()
    elif escolha == 3:
        verificar_situacao()
    elif escolha == 4:
        print("Saindo...")
    else:
        print("Digite um número de ação válido!")
        menu()

menu()
