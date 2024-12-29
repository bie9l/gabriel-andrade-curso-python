    
class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    def Subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print(f"Nº do andar atual: {self.atualAndar}, Subindo.")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def Descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print(f"Nº do andar atual: {self.atualAndar}, Descendo.")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print(f"Nº atual de pessoas: {self.atualCapacidade}, entrando uma pessoa.")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade >= 1:
            self.atualCapacidade -= 1
            print(f"Nº atual de pessoas: {self.atualCapacidade}, saindo uma pessoa.")
        else:
            print("NÃO TEM NINGUÉM")

elevador = Elevador(totalCapacidade=5, atualCapacidade=0, totalAndar=10, atualAndar=0)

elevador.Subir()
elevador.Entrar()
elevador.Descer()
elevador.Sair()