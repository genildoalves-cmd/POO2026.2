

from Excecoes import ValorInvalido


class ContaBancaria:
    
    def __init__(self, valor=0):
        self.valor = valor

    @property
    def saldo(self):
        return self._valor

    def sacar(self,valor):
    
        if valor <= 0:
        
            raise ValorInvalido("valor menor que 0")
    
        if valor > self.saldo:
        
            raise ValorInvalido("valor maior que saldo informe valor menor")
    
        self.valor-= valor
    
    def depositar(self, valor):
    
        if valor <= 0:
        
         raise ValorInvalido("valor menor que zero")
        
        self.valor += valor
        
        
     
    