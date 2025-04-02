# second assignment to insert "..." in between every word of the string passed

playback = input("Enter string")

new_string = ""

for i in range(len(playback)):
    if playback[i] != " ":
        new_string += playback[i]
    else:
        new_string += "..."

print(new_string)

