# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.




def main():
    amount_due = 50
    print("Amount due :", amount_due)

    while amount_due > 0:
        coin = int(input("Insert coin: "))

        if coin == 25:
            amount_due -= 25
        elif coin == 10:
            amount_due -= 10
        elif coin == 5:
            amount_due -= 5
        # else:
        #     print("Enter 5,10,25")

        amount_due_check(amount_due)

def amount_due_check(amount):
    if amount <= 0:
        print("Change owed:", abs(amount))
    else:
        print("Amount Due:",abs(amount))


if __name__ == "__main__":
    main()



