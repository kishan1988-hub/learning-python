def main():
    x = int(input("What's X?"))
    if is_even(x):
        print("Value of X is even")
    else:
        print("Value of X is odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:                 # both can be used, below is very much python
    #     return False
    # second option
    #return True if n % 2 == 0 else False
    # third option
    return n % 2 == 0
main()