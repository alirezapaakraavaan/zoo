class Animal():
    def __init__(self, type, color, name):
        self.type = type
        self.color = color
        self.name = name

    def fly(self):
        print("Not Defined")
    

    def run(self):
        print("Not Defined")

    
    def __repr__(self) -> str:
        return "Error"