

class Animal:
    def __init__(self,nome:str)-> None:
        self.nome=nome
        self.posicao = 0

    def mover_se(self)-> None:
        self.poicao += 1

class Gato(Animal):

    def mover_se(self)-> None:
        print(f"{self.nome}  caminhando ....")
        self.posicao += 1

class Peixe(Animal):
    def mover_se(self)-> None:
        print(f"{self.nome}  nadando .... ")
        self.posicao += 1

class Cobra(Animal):
    def mover_se(self)-> None:
        print(f"{self.nome} rastejando ...")
        self.posicao += 1

def mover_todos(animais : list[Animal]) -> None:
    for animal in animais:
        animal.mover_se() # Polimofismo

zoologico = [Gato("tom")
             ,Peixe("Nemo")
             ,Cobra("Nadja")]

mover_todos(zoologico)