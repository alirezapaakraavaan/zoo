from src.Animal import Animal

def main():
    lion = Animal("Mamel", "Yellow", "King")
    bird = Animal("Bird", "Black", "sam")

    print(lion.run(lion.name))
    print(bird.fly(bird.name))

main()