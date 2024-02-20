from src.Lions import Lions
from src.Birds import Birds

def main():
    lion = Lions("Mamel", "Yellow", "King")
    bird = Birds("Bird", "Black", "sam")

    lion.run()
    bird.fly()

main()