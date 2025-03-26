name = input("What's your name? ")

# if name == "Harry":
#     print ("Gryffindor")
# elif name == "Hermonie":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")
match name:
    # case "Harry":
    #     print("Gryffindor")
    # case "Hermonie":
    #     print("gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Harry" | "Hermonie" | "Ron":
        print("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("Who??")  # Handle else option