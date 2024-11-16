class Aluno():
    notas = { 'historia': [9.2, 8,7, 6]} # estrutura do registro da nota (dict, cujo os valores das chaves são listas com as notas)
    def __init__(self, nome, idade, ano, matricula):
        self.nome = nome
        self.idade = idade
        self.ano = ano
        self.matricula = matricula

class Professor():
    def __init__(self, nome, idade, salario, especialidade):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.especialidade = especialidade

class Escola():
    dados_escola = []
    matriculados = []
    funcionarios = []
    def __init__(self, nome, endereco, segmento):
        self.nome = nome
        self.endereco = endereco
        self.segmento = segmento

    def cadastrar_escola(self):
        print('Cadastro de escola!')
        nome = input('Digite o nome da escola: ')
        endereco = input('Digite o endereço da escola: ')
        segmento = input('Digite o segmento da escola: ')
        escola = Escola(nome, endereco, segmento)
        self.dados_escola.append(escola)
        self.menu()

    def matricular(self):
        print('Cadastro de aluno!')
        nome = input('Digite o nome do aluno: ')
        idade = input('Digite a idade do aluno: ')
        ano = input('Digite o ano em que o aluno esta: ')
        matricula = input('Digite o numero de matricula do estudante: ')
        aluno = Aluno(nome, idade, ano, matricula)
        self.matriculados.append(aluno.__dict__)
        self.menu()

    def cadastrar_professor(self):
        print('Cadastro de professor!')
        nome = input('Digite o nome do professor: ')
        idade = input('Digite a idade do professor: ')
        salario = input('Digite o salario que o professor ganha: ')
        especialidade = input('Digite a especialidade do professor: ')
        professor = Professor(nome, idade, salario, especialidade)
        self.funcionarios.append(professor.__dict__)
        self.menu()

    def menu(self):
        print('Bem vindo ao menu de cadastramento da escola! :)')
        print("Escolha sua ação com os numeros de 1 a 3:")
        print('-'*10)
        print('1 - Cadastrar escola', '2 - Registrar professores', "3 - Cadastrar alunos", "4 - Lançar notas", "5 - Ver professores cadastrados", "6 - Sair", sep='\n')
        print('-'*10)
        escolha = int(input('Qual ação deseja realizar ? Digite o numero correspondente a ela: '))
        if escolha == 1:
            self.cadastrar_escola()
        elif escolha == 2:
            self.cadastrar_professor()
        elif escolha == 3:
            self.matricular()
        elif escolha == 4:
            self.lançar_notas()
            pass
        elif escolha == 5:
            print(self.funcionarios)
            self.menu()
        elif escolha == 6:
            pass
        else:
            print("Digite um numero de ação válido !")


escola1 = Escola('nome', 'endereco', 'segmento')

escola1.menu()





#1 - cadastre uma escola, registre um professor de matematica, historia, ciencias e portugues

#2 - verifique a lista de professores cadastrados

#3 - matricule 5 alunos

#4 - lance notas (pelo menos 3 de cada materia para cada aluno matriculado)


