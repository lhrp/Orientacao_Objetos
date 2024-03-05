import sqlite3
import time

class Produto:
    def __init__(self, nCdProduto, cNmProduto=None, cDescricao=None, dValidade=None):
        self.nCdProduto = nCdProduto
        self.cNmProduto = cNmProduto
        self.cDescricao = cDescricao
        self.dValidade = dValidade

    def configurar_nome(self, cNmProduto):
        self.cNmProduto = cNmProduto

    def configurar_descricao(self, cDescricao):
        self.cDescricao = cDescricao

    def configurar_validade(self, dValidade):
        self.dValidade = dValidade

    def exibir_informacoes(self):
        print(f"Informações do produto: Código - {self.nCdProduto}, Nome - {self.cNmProduto}, Descrição - {self.cDescricao}, Validade - {self.dValidade}")

class ProdutoDB:
    def __init__(self):
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

    def cadastrar(self, produto):
        self.cur.execute('''INSERT INTO produtos (nome, descricao, validade) 
                            VALUES (?, ?, ?)''', (produto.cNmProduto, produto.cDescricao, produto.dValidade))
        self.conn.commit()
        print("Produto cadastrado com sucesso.")

    def consultar(self, codigo):
        self.cur.execute('''SELECT * FROM produtos WHERE codigo=?''', (codigo,))
        produto = self.cur.fetchone()
        if produto:
            return Produto(produto[0], produto[1], produto[2], produto[3])
        else:
            print("Produto não encontrado.")
            return None

    def atualizar(self, produto):
        self.cur.execute('''UPDATE produtos SET nome=?, descricao=?, validade=? WHERE codigo=?''', (produto.cNmProduto, produto.cDescricao, produto.dValidade, produto.nCdProduto))
        self.conn.commit()
        print("Produto atualizado com sucesso.")

    def apagar(self, codigo):
        self.cur.execute('''DELETE FROM produtos WHERE codigo=?''', (codigo,))
        self.conn.commit()
        print("Produto apagado com sucesso.")


interagirProduto = ProdutoDB()

produto_consultado = interagirProduto.consultar(1)
if produto_consultado:
    produto_consultado.exibir_informacoes()



# # Exemplo de uso
# produto_dao = ProdutoDB()

# # Criando um novo produto
# novo_produto = Produto(0, "Produto 00", "Produto de Exemplo", time.strftime("%Y-%m-%d"))

# # Cadastrando o produto
# produto_dao.cadastrar(novo_produto)

# # Consultando o produto cadastrado
# produto_consultado = produto_dao.consultar(novo_produto.nCdProduto)
# if produto_consultado:
#     produto_consultado.exibir_informacoes()

# # Atualizando o produto
# produto_consultado.configurar_nome("Novo Produto 00")
# produto_consultado.configurar_descricao("Nova Descrição")
# produto_consultado.configurar_validade(time.strftime("%Y-%m-%d"))
# produto_dao.atualizar(produto_consultado)

# # Consultando o produto atualizado
# produto_atualizado = produto_dao.consultar(novo_produto.nCdProduto)
# if produto_atualizado:
#     produto_atualizado.exibir_informacoes()

# # Apagando o produto
# produto_dao.apagar(novo_produto.nCdProduto)
