import sqlite3
import time

class Produto:
    def __init__(self, nCdProduto, cNmProduto, cDescricao, dValidade):
        self.nCdProduto = nCdProduto
        self.cNmProduto = cNmProduto
        self.cDescricao = cDescricao
        self.dValidade = dValidade
        self.conn = sqlite3.connect('produtos.db')
        self.cur = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            codigo INTEGER PRIMARY KEY,
                            nome TEXT,
                            descricao TEXT,
                            validade TEXT)''')
        self.conn.commit()

    def cadastrar(self):
        self.cur.execute('''INSERT INTO produtos (nome, descricao, validade) 
                            VALUES (?, ?, ?)''', (self.cNmProduto, self.cDescricao, self.dValidade))
        self.conn.commit()
        print("Produto cadastrado com sucesso.")

    def consultar(self):
        self.cur.execute('''SELECT * FROM produtos WHERE codigo=?''', (self.nCdProduto,))
        produto = self.cur.fetchone()
        if produto:
            print(f"Informações do produto: Código - {produto[0]}, Nome - {produto[1]}, Descrição - {produto[2]}, Validade - {produto[3]}")
        else:
            print("Produto não encontrado.")

    def atualizar(self, cNmProduto=None, cDescricao=None, dValidade=None):
        if cNmProduto:
            self.cNmProduto = cNmProduto
        if cDescricao:
            self.cDescricao = cDescricao
        if dValidade:
            self.dValidade = dValidade
        self.cur.execute('''UPDATE produtos SET nome=?, descricao=?, validade=? WHERE codigo=?''', (self.cNmProduto, self.cDescricao, self.dValidade, self.nCdProduto))
        self.conn.commit()
        print("Produto atualizado com sucesso.")

    def apagar(self):
        self.cur.execute('''DELETE FROM produtos WHERE codigo=?''', (self.nCdProduto,))
        self.conn.commit()
        print("Produto apagado com sucesso.")

# Criando um novo produto
novoProduto = Produto(1, 0, 0, 0)

# Operações CRUD
#novoProduto.cadastrar()
novoProduto.consultar()
#novoProduto.atualizar(cNmProduto="Novo Produto 00", cDescricao="Nova Descrição", dValidade=time.strftime("%Y-%m-%d"))
novoProduto.consultar()
#novoProduto.apagar()
