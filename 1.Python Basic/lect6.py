#conditional statements
# if,elif,else
# nested conditional statements

marks = 16
if marks >= 10:
    print("You have passed")
# elif
elif marks >= 5:
    print("You have passed with marginal marks")
# else
else:
    print("You have failed")


# Nested conditional statements
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is not positive")