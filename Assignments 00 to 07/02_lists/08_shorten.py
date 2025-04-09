MAX_LENGTH = 3  # You can change this value to test your program

def shorten(lst):
    """
    Removes elements from the end of lst and prints each item it removes
    until the list is MAX_LENGTH items long.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item from the list
        print("Removed:", removed_item)

def main():
    lst = input("Please enter a list of elements separated by spaces: ").split()
    shorten(lst)  # Call the shorten function on the list

if __name__ == '__main__':
    main()
# The program will prompt the user to enter a list of elements separated by spaces.
# It will then remove elements from the end of the list until the list is MAX_LENGTH items long,
# printing each removed item as it goes. If the list is already at or below MAX_LENGTH, it will do nothing.
# The program will print the removed items to the console.
# The final list will be printed to the console.
# The program will end when the user presses enter without typing anything.
# The program will not return any value.
# The program will not raise any exceptions.
# The program will not handle any exceptions.
# The program will not use any external libraries.
# The program will not use any external files.
# The program will not use any external modules.
# The program will not use any external packages.