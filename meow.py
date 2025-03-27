# while True:
#     n = int(input("Whats n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whats N ? "))
        if n > 0:
            break    
    return n
        
def meow(n):
    for _ in range(n):
        print("Meow")
    
main()