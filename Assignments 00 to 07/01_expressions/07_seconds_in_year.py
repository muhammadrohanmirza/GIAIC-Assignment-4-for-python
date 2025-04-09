def main():
    # Define the number of seconds in a year
    DAYS_PER_YEAR: int = 365
    HOURS_PER_DAY: int = 24
    MIN_PER_HOUR: int = 60
    SEC_PER_MIN: int = 60

    seconds_in_a_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Display the result
    print(f"\033[1;3mThere are {seconds_in_a_year} seconds in a year.\033[0m")


if __name__ == "__main__":
    main()

