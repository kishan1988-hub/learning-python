# third assignment for converting :) into smiley faces - simple string replacement function being called


def main ():
    string = input("Enter a string: ")

    converted_string = convert(string)

    print(converted_string)

def convert(string):
    string = string.replace(":)", "🙂")

    string = string.replace(":(", "🙁")

    return string

main()

