import os

os.system("cls")

class Produto:
    def __init__(self, nCdProduto, cNmProduto=None, cDescricao=None, dValidade=None):
        self.nCdProduto = nCdProduto
        self.cNmProduto = cNmProduto
        self.cDescricao = cDescricao
        self.dValidade = dValidade

    def atualizarNome(self, cNmProduto):
        self.cNmProduto = cNmProduto

    def atualizarDescricao(self, cDescricao):
        self.cDescricao = cDescricao

    def atualizarValidade(self, dValidade):
        self.dValidade = dValidade

    def exibirDados(self):
        print(f"Informações do produto: \nCódigo: {self.nCdProduto}\nNome: {self.cNmProduto}\nDescrição: {self.cDescricao}\nValidade: {self.dValidade}")


exemplo = Produto(1, "Teste1", "Descricao", "22221122")

exemplo.exibirDados()

exemplo.atualizarDescricao("Nova Descricao")
print("\n\n")
exemplo.exibirDados()
print("\n\n")

print(type(exemplo))