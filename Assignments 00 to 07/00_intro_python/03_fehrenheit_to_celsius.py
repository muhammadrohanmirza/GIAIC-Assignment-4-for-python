def main():

    fehrenheit = float(input("\033[1;3m what's the temperature in fehrenheit___?\033[0m"))
    # Convert fehrenheit to celsius
    
    celsius = (fehrenheit - 32) * 5.0/9.0
    # Print the result
    
    print(f"temperature: {fehrenheit}F = {celsius}C")    

if __name__ == "__main__":
    main()