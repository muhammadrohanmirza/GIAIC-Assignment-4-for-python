def main():
    # User se year lo
    year = int(input("Konsa saal check karna hai? "))
    # Leap year ka check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Yeh Leap Year hai!")
    else:
        print("Yeh Leap Year nahi hai.")
    # # There is no need to edit code beyond this point
if __name__ == '__main__':
    main()