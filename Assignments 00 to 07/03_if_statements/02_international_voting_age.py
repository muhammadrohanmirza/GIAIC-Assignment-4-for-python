# Ask the user for their age
age = int(input("How old are you? "))

# Voting ages in fictional countries
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

# Check for Peturksbouipo
if age >= PETURKSBOUIPO_AGE:
    print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
else:
    print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

# Check for Stanlau
if age >= STANLAU_AGE:
    print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
else:
    print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

# Check for Mayengua
if age >= MAYENGUA_AGE:
    print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
else:
    print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
