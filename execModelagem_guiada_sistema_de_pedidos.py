
class Produto:
    def __init__(self, nome:str,
                 preco: float) -> None:
       self.nome = nome
       self.preco = preco

class ItemPedido:
   def __init__(self, produto: Produto,
                 quantidade: int) -> None:
      self.produto =  produto
      self.quantidade = quantidade
   @property
   def subtotal(self) -> float:
       return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self,cliente:"Cliente") -> None:

        self.cliente = cliente # associacao
        self._itens: list[ItemPedido] = []


    def adicionar(self, produto:Produto,
                  quantidade: int) -> None:
     item = ItemPedido(produto, quantidade)
     self._itens.append(item)  # composicao

    
    @property
    def total(self) ->float:
        return sum(i.subtotal for i in self.itens)

class ItensTotal:
    def __str__(self, totalitens: int , total: int)->int:
        self.totalitens=totalitens
        self.total=total
       


   