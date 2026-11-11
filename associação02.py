class Interruptor:
    def __init__(self, compartimento: str) -> None:
        self.compartimento = compartimento

    def Botao_ligar(self) -> None:
        print(f" e a luz acendeu na {self.compartimento} ")

    def Botao_desligar(self) -> None:
        print(f" e a luz apagou na {self.compartimento}")


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def ligar_lampada(self, inter: Interruptor):
        print(f" lampada ligada por {self.nome}", end="")
        inter.Botao_ligar()

    def desligar_lampada(self, inter: Interruptor):
        print(f" Lampada desligada por {self.nome}" , end="")
        inter.Botao_desligar()


maria = Pessoa("Maria")
sala = Interruptor("sala")
maria.ligar_lampada(sala)
joao = Pessoa("Joao")
joao.desligar_lampada(sala)
