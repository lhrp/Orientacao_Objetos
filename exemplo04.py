import time
from exemplo03 import ProdutoDB, Produto

# Exemplo de uso
ProdutoDB()

# Criando um novo produto
dadosProduto = Produto(0, "Produto 07", "Produto de Exemplo", time.strftime("%Y-%m-%d"))

# Cadastrando o produto
ProdutoDB().cadastrar(dadosProduto)