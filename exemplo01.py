import time

class Produto:
    def __init__(self, nCdProduto, cNmProduto, cDescricao, dValidade):
        self.nCdProduto = nCdProduto
        self.cNmProduto = cNmProduto
        self.cDescricao = cDescricao
        self.dValidade = dValidade

    def Cadastrar(self):
        print(f"Produto cadastrado: Código - {self.nCdProduto}, Nome - {self.cNmProduto}")

    def Consultar(self):
        print(f"Informações do produto: Código - {self.nCdProduto}, Nome - {self.cNmProduto}, Descrição - {self.cDescricao}, Validade - {self.dValidade}")

    def Atualizar(self, cNmProduto=None, cDescricao=None, dValidade=None):
        if cNmProduto:
            self.cNmProduto = cNmProduto
        if cDescricao:
            self.cDescricao = cDescricao
        if dValidade:
            self.dValidade = dValidade
        print("Produto atualizado com sucesso.")

    def Apagar(self):
        del self.nCdProduto
        del self.cNmProduto
        del self.cDescricao
        del self.dValidade
        print("Produto apagado.")

# Criando um novo produto
novoProduto = Produto(0, "Produto 00", "Produto de Exemplo", time.strftime("%Y-%m-%d"))

# Operações CRUD
novoProduto.Cadastrar()
novoProduto.Consultar()
novoProduto.Atualizar(cNmProduto="Novo Produto 00", cDescricao="Nova Descrição", dValidade=time.strftime("%Y-%m-%d"))
novoProduto.Consultar()
novoProduto.Apagar()
