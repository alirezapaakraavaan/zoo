from src.Animal import Animal

class Lions(Animal):

    def run(self):
        print(f"{self.name} runs")

    def __repr__(self) -> str:
        return f"{self.name} runs"