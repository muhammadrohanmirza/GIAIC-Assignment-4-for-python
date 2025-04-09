SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Prompt the user for input
    adjective: str = input("Enter an adjective: ")
    noun: str = input("Enter a noun: ")
    verb: str = input("Enter a verb: ")

    # Create the mad lib sentence
    mad_lib_sentence: str = SENTENCE_START + adjective + " " + noun + " " + verb + "."

    # Display the mad lib sentence
    print(mad_lib_sentence)

if __name__ == "__main__":
    main()