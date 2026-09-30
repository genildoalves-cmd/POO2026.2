class Tarefa:
    def __init__(self, titulo: str) -> None:

        self.titulo = titulo
        
    def __str__(self) -> str :

        return f"Tarefa:{self.titulo}"

p = Tarefa("A bigorna")
print(p)
print(f"Item:{p}")
