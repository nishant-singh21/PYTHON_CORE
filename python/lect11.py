# while loop ,break , continue 

# syantax: while condition: do anything
# while loop is used to execute a block of code repeatedly as long as the condition is true.
num =1
while num <= 10:
    print(num)
    num += 1


num = 10 
while num >= 1:
    print(num)
    num -= 1

# break statement : it is used to terminate the loop when a certain condition is met
i = 1
while i <=10:
    if i == 5:
        break
    print(i)
    i += 1

# continue statement : it is used to skip the current iteration of the loop and move to the next iteration
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

