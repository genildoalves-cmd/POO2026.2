class interruptor:
    
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def Acionar(self) -> None:
        print(f" e a luz da {self.comodo} acendereu !")
    
    def Desligar(self) -> None:
        print(f" e a luz da {self.comodo} desligou !")    
    

class Pessoa:
    
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def Ligar_lampada(self, inter: interruptor) -> None:
        print(f"{self.nome} foi ate a parede", end="")
        inter.Acionar()
        
    def Desligar_lampada(self, inter: interruptor) -> None:
        print(f"{self.nome} foi ate a parede ", end="")
        inter.Desligar()


maria = Pessoa("maria")
joao = Pessoa("Joao")
sala = interruptor("sala")
maria.Ligar_lampada(sala)
joao.Desligar_lampada(sala)