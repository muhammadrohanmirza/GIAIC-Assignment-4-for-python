def main():
    # Get user input
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number ** 2
    
    # Print the result
    print(f"The square of {number} is {square}")

if __name__ == '__main__':
    main()