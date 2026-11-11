class Produtos:
    
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f" Produto: {self.nome} e o valor é : {self.valor}"


class Carrinho:
    
    def __init__(self):
        self.itens: list[Produtos] = []

    def adicionar_itens(self, produto: Produtos):
        self.itens.append(produto)

    def listar_produtos(self):
        
        if not self.itens:
            print("produto vazio")
            
        else:
         for produto in self.itens:
             print(produto)


papel = Produtos("papel", 2.50)
agua = Produtos("agua", 1.50)
carrinho = Carrinho()
#carrinho.listar_produtos()
carrinho.adicionar_itens(papel)
carrinho.adicionar_itens(agua)
carrinho.listar_produtos()
