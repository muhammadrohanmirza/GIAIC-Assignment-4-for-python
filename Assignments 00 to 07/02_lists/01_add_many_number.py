def main():
    # Get the first number from the user
    first_number = input("Enter a number: ")

    # Initialize the sum with the first number
    total_sum = int(first_number)

    # Loop to get more numbers from the user
    while True:
        # Ask for another number or to stop
        next_number = input("Enter another number (or 'stop' to finish): ")
        
        if next_number.lower() == "stop":
            break

        # Check if the input is a number
        if not next_number.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
    
        # Add the new number to the total sum
        total_sum += int(next_number)

        # Print the current sum after each addition
        print("Current sum:", total_sum)


    # Print the final sum
    print("The total sum is:", total_sum)

if __name__ == "__main__":
    main()