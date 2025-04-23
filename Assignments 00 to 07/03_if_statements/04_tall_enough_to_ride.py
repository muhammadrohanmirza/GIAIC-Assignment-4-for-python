# Pre-specified minimum height for the ride
min_height = 50

# Boilerplate code for the Python program
def tall_enough_extension():
    while True:
        # Ask the user for their height
        height_input = input("How tall are you (height in 'inch')? ")
        
        # If the input is empty, stop the program
        if height_input == "":
            print("Goodbye!")
            break
        
        # Try to convert the input to an integer
        try:
            height = int(height_input)
        except ValueError:
            print("Please enter a valid number for height.")
            continue
        
        # Check if the user is tall enough to ride
        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Entry point for the program
if __name__ == "__main__":
    tall_enough_extension()
