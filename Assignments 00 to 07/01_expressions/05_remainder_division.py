def main():
    # Get the dividend and divisor from the user
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    # Calculate the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Display the results
    print(f"The quotient is: {quotient}")
    print(f"The remainder is: {remainder}")

if __name__ == "__main__":
    main()  