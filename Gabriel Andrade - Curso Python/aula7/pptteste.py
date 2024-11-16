from random import randint

opcoes = ["pedra", "papel", "tesoura"]
aleatorio = randint(0,2)

def iniciar():  
    print("Escolha o que deseja mostrar: ")
    print("0 para Pedra", "1 para papel", "2 para tesoura", sep='\n')
    ganhador()
    fim_de_jogo()

def ganhador():
    while True:
        try:
            escolha_usuario = int(input('Qual sua escolha: '))
            if escolha_usuario == aleatorio:
                print("Empate")
            elif escolha_usuario == 0 and aleatorio == 2 or escolha_usuario == 1 and aleatorio == 0 or escolha_usuario == 2 and aleatorio == 1:
                print('Você ganhou !')
            elif escolha_usuario == 0 and aleatorio == 1 or escolha_usuario == 1 and aleatorio == 2 or escolha_usuario == 2 and aleatorio == 0:
                print('Você perdeu !')
            else:
                print('Escolha uma opção válida!')
                continue
            print(f'A máquina escolheu {opcoes[aleatorio]}')
            break
        except ValueError:
            print("Por favor, digite um numero valido. ")

def fim_de_jogo():
    while True:
        try:
            print("Fim de jogo!")
            print("-"*10)
            print("O que deseja realizar agora ? ")
            print("-"*10)
            print("1 para Jogar novamente", "2 para Sair", sep='\n')
            pos_jogo = int(input('Qual sua escolha: '))
            if pos_jogo == 1:
                iniciar()
            elif pos_jogo == 2:
                pass
            else:
                print('Escolha uma opção válida!')
            break
        except ValueError:
            print("Por favor, digite uma opção valida. ")

    
iniciar()
