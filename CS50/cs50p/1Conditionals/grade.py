score = int(input("Score: "))

if 90 <= score <= 100:
    # Or (assured of user input being an int below 101)
    # if score >= 90
    print("Grade: A")
# if score >= 80:
elif 80 <= score <= 90:
    print("Grade: B")
# if score >= 70:
elif 70 <= score <= 80:
    print("Grade: C")
# if score >= 60:
elif 60 <= score <= 70:
    print("Grade: D")
else:
    print("Grade F")