import math


def main():
    # Get the lengths of the two legs from the user
    ab = float(input("Enter the length of leg AB: "))
    ac = float(input("Enter the length of leg AC: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc : float = math.sqrt(ab**2 + ac**2)   

    # Display the result
    print(f"The length of BC is: {bc:.2f}")
if __name__ == "__main__":
    main()