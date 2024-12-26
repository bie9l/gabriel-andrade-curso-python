import sqlite3
from datetime import datetime

class Produto:
    def __init__(self, id, nome, descricao, quantidade, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

class Venda:
    def __init__(self, id_venda, id_produto, quantidade_vendida, data_venda):
        self.id_venda = id_venda
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

class GerenciadorEstoque:
    def __init__(self, db_name='estoque.db'):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabelas()

    def criar_tabelas(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS vendas (
                    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_produto INTEGER,
                    quantidade_vendida INTEGER,
                    data_venda TEXT,
                    FOREIGN KEY(id_produto) REFERENCES produtos(id)
                )
            ''')

    def adicionar_produto(self, nome, descricao, quantidade, preco):
        with self.conn:
            self.conn.execute('''
                INSERT INTO produtos (nome, descricao, quantidade, preco)
                VALUES (?, ?, ?, ?)''', (nome, descricao, quantidade, preco))

    def atualizar_produto(self, id, quantidade):
        with self.conn:
            self.conn.execute('''
                UPDATE produtos
                SET quantidade = ?
                WHERE id = ?
            ''', (quantidade, id))

    def visualizar_produtos(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM produtos')
            for row in cursor:
                print(row)

    def registrar_venda(self, id_produto, quantidade_vendida):
        with self.conn:
            produto = self.conn.execute('SELECT * FROM produtos WHERE id = ?', (id_produto,)).fetchone()
            if produto and produto[3] >= quantidade_vendida:
                nova_quantidade = produto[3] - quantidade_vendida
                self.conn.execute('''
                    INSERT INTO vendas (id_produto, quantidade_vendida, data_venda)
                    VALUES (?, ?, ?)''', (id_produto, quantidade_vendida, datetime.now().isoformat()))
                self.atualizar_produto(id_produto, nova_quantidade)
            else:
                print("Estoque insuficiente ou produto não encontrado.")

    def gerar_relatorio_estoque(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM produtos')
            relatorio = cursor.fetchall()
            for row in relatorio:
                print(row)

if __name__ == "__main__":
    gerenciador = GerenciadorEstoque()

    # Menu
    print("Gerenciador de Estoque")
    print("1. Adicionar Produto")
    print("2. Visualizar Produtos")
    print("3. Registrar Venda")
    print("4. Gerar Relatório de Estoque")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    while opcao != 5:
        if opcao == 1:
            nome = input("Nome do Produto: ")
            descricao = input("Descricão do Produto: ")
            quantidade = int(input("Quantidade em Estoque: "))
            preco = float(input("Preço do Produto: "))
            gerenciador.adicionar_produto(nome,descricao, quantidade, preco)
        elif opcao == 2:
            gerenciador.visualizar_produtos()
        elif opcao == 3:
            id_produto = int(input("ID do Produto: "))
            quantidade_vendida = int(input("Quantidade vendida: "))
            gerenciador.registrar_venda(id_produto, quantidade_vendida)
        elif opcao == 4:
            gerenciador.gerar_relatorio_estoque()
        opcao = int(input("Escolha uma opção: "))
