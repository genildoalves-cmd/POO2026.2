


class aluno:

    def __init__ (self,nome:str, matricula:str)->None:
        self.nome=nome
        self.matricula=matricula
        self.notas: list[float]=[]

    def lançar_nota(self,valor:float)->None:
        self.notas.append(valor)        

    def media(self)->float:
        if not self.notas:
            return 0.0
        return sum(self.notas)/len(self.notas)

    def aprovado(self)->bool:
        return self.media() >= 6.0
    def __str__(self)->str:
        return f"{self.nome} ({self.matricula}) - media:{self.media():.1f}"
    
aluno1 = aluno("João", "202401")
aluno1.lançar_nota(8.0)
aluno1.lançar_nota(6.0)

print(aluno1)
print(f"Aprovado: {aluno1.aprovado()}")


    