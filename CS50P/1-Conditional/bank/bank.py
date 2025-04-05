# This program evaluates a user-input greeting and assigns a numerical value based on specific conditions. It then prints the assigned value with a "$" symbol.

# Usage:
# 1. Run the program.
# 2. Enter a greeting when prompted.
# 3. The program will evaluate the greeting and print the assigned value with a "$" symbol.

# Greeting Value Assignments:
# - If the greeting contains "hello" (case-insensitive), the value is assigned as $0.
# - If the greeting starts with the letter "h" (case-sensitive), the value is assigned as $20.
# - If none of the above conditions are met, the value is assigned as $100.

# Example:
# Greeting: Hello, how are you?
# $0


def main():

    val = input("Greeting: ")
    #val = val.lower()
    result = valid(val)
    print (f"${result}")

def valid(val):
    val = val.lower().strip()

    if "hello" in val :
        return 0
    elif val[0]== "h":
        return 20
    else:
        return 100




main()
