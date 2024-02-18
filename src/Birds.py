from src.Animal import Animal

class Birds(Animal):
    
    def __repr__(self, name) -> str:
        return f"{name} flys"