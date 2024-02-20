from src.Animal import Animal

class Birds(Animal):
    
    def fly(self):
        print(f"{self.name} flys")

    def __repr__(self) -> str:
        return f"{self.name} flys"