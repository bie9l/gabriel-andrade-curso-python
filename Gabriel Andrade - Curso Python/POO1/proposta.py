

A classe Elevador também possui os seguintes métodos:



Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo". Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".



Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".



Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".



Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".




o que eu fiz:
    
    
class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    def Subir(self):
        if atualAndar < totalAndar:
            print(f"Nº do andar atual: {atualAndar}, Subindo.")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
    
    def Descer(self):
        if atualAndar > 1:
            print(f"Nº do andar atual: {atualAndar}, Descendo.")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
    
    def Entrar(self):
        if atualCapacidade < totalCapacidade:
            print(f"Nº atual de pessoas: {atualCapacidade}, entrando uma pessoa.")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")
    
    def Sair(self):
        if atualCapacidade => 1:
            print(f"Nº atual de pessoas: {atualCapacidade}, saindo uma pessoa.")
        else:
            print("NÃO TEM NINGUÉM")
            
            
            
            
corrigido:
    
    class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    def Subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1  # Incrementa o andar atual
            print(f"Nº do andar atual: {self.atualAndar}, Subindo.")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def Descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1  # Decrementa o andar atual
            print(f"Nº do andar atual: {self.atualAndar}, Descendo.")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1  # Incrementa a capacidade atual
            print(f"Nº atual de pessoas: {self.atualCapacidade}, entrando uma pessoa.")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade >= 1:
            self.atualCapacidade -= 1  # Decrementa a capacidade atual
            print(f"Nº atual de pessoas: {self.atualCapacidade}, saindo uma pessoa.")
        else:
            print("NÃO TEM NINGUÉM")

# Exemplo de uso
elevador = Elevador(totalCapacidade=5, atualCapacidade=0, totalAndar=10, atualAndar=0)

# Testando os métodos
elevador.Subir()
elevador.Entrar()
elevador.Descer()
elevador.Sair()