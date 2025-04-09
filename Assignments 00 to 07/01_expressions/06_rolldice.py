
import random

num_sides = 6  # Number of sides on the die

def main():

    dice1: int = random.randint(1, num_sides)  # Roll the first die
    dice2: int = random.randint(1, num_sides)  # Roll the second die


    # Calculate the sum of the two dice
    total_dice: int = dice1 + dice2

    # Display the results
    print("Dice have" , num_sides, "sides each.")
    print("First Dice:", dice1)
    print("Second Die:", dice2)
    print("Total Dice:", total_dice)

if __name__ == "__main__":
    main()