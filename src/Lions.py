from src.Animal import Animal

class Lions(Animal):

    def __repr__(self, name) -> str:
        return f"{name} runs"