def main():
#     print_column(3)
#     print_row(4)

# def print_column(height):
#     for _ in range(height):
#         print("#")
# def print_row(width):
#     print("?" * width)

        print_square(3)

def print_square(size):
        # for each of row
        for i in range(size):
                # for each of brick in row
                for j in range(size):
                        # printing each brick
                        print("#", end="") # does not open new line & prints all # in same line for each iteration
                print() # in each iteration moves cursor to next line
main()