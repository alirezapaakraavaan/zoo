class Animal():
    def __init__(self, type, color, name):
        self.type = type
        self.color = color
        self.name = name

    def fly(self, name):
        return f"{self.name} flys"
    

    def run(self, name):
        return f"{self.name} runs"
    
    def __repr__(self) -> str:
        return None