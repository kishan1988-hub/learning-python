score = int(input("Score: "))

# if score>=90 and score <=100:
#     print("Grade is A")
# elif score >= 80 and score <=90:
#     print("Grade is B")
# elif score >=70  and score <=80:
#     print("Grade is C")

# elif score >=60  and score <=70:
#     print("Grade is D")

if 90 <= score <= 100:
    print("Grade : A") 
elif 80 <= score <= 90:
    print("Grade : B")
elif 70 <= score <= 80:
    print("Grade : C")
else:
    print("Grade F")