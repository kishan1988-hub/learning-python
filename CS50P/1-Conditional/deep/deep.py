# This program prompts the user to enter their answer to the Great Question of Life, the Universe, and Everything and checks if their input matches one of the expected answers.

# Usage:
# 1. Run the program.
# 2. Enter an answer when prompted.
# 3. The program will check if the entered answer matches "42," "forty two," or "forty-two" (case-insensitive) and print "Yes" if there is a match, or "No" otherwise.

# Example:
# What is the Answer to the Great Question of Life, the Universe, and Everything? 42
# Yes
# prompt to get value 
val = input ("Whats the answer to the Greatest question of life, the universe, and Everything ? ")

if val.strip() == "42" :
    print("Yes")
elif val.lower() == "forty-two":
    print("Yes")
elif val.lower() == "forty two":
    print("Yes")
else:
    print("No")
