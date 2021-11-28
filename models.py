class Posto:
    def __init__(self, preco, produto, bairro, nome, bandeira, id=None):
        self.id = id
        self.preco = preco
        self.produto = produto
        self.bairro = bairro
        self.nome = nome
        self.bandeira = bandeira

    def getBairro(self, bairro):
        self.bairro = bairro
