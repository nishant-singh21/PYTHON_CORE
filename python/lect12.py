# for loop , usses and syntax
# break statement , continue statement
# pass 


# for loop is used to iterate over a sequence (such as a list, tuple,dictionary, set, or string)
#  and execute a block of code for each item in the sequence.
# 
# syantax :for variable in sequence:
#          body  of the loop 

    # uses of for loop 
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# loops with lists
name = 'Mohit '
for char in name:
    print(char)
    if char == 'h':
        break

else:
    print('loop is completed')


# for lop with range function

for i in range(5, 11):
    # print(i)
    if i%2 == 0:
        print(i, "is even")


# inrange we use nested for loop

for i in range(1, 4):
    for j in range(1, 3):
        print('i : {i}, j : {j}'.format(i=i, j=j))