#criar a classe cachorro com os atributos, parametros, metodos e o objeto


class Cachorro:
    def __init__(self, nome, raca, cor, status, peso, comida, altura, idade):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.status = status
        self.peso = peso
        self.comida = comida
        self.altura = altura
        self.idade = idade

    def correr(self):
        self.status = 'correndo'

    def brincar(self):
        self.status = 'brincando'

    def comer(self):
        msg = f'Pluto esta comendo'
        self.status = 'comendo'
        print(msg)
        return msg

        def latir(self):
            self.latir = 'latindo'


pluto = Cachorro('pluto', 'vira-lata', 'preto', 'parado', '20kg', 'ração', '1,50cm', '10 anos')

print(f'Meu cachorro pluto esta {pluto.status}')

pluto.correr()

print(f'Meu cachorro pluto esta {pluto.status}')

pluto.comer()