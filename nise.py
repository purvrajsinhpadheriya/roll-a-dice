import random

def roll_dice():
    dice_faces = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----"
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----"
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----"
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----"
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----"
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----"
        )
    }
    
    return dice_faces[random.randint(1, 6)]

def main():
    while True:
        input("Press enter to roll the dice...")
        dice_face = roll_dice()
        for line in dice_face:
            print(line)
        print("Press 'y' to roll again or 'n' to exit: ", end="")
        choice = input().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()

