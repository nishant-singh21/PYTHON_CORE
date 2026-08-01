# user define fundstion today i learned about user define function in python

num1 = 10 
num2 =  20 
sum = num1 + num2
print('sum of two number is ',sum)

#  repetations of code is not good practice so we can use function to avoid repetation of code

def sum(a , b):
    add = a + b
    print('sum of two number is ',sum)
sum(10,20)
sum(1, 2) 
print('end of the funtion call')



#  return statement in function
def sum(a, b):
    return a + b
add = sum(10, 20)
print(add)


def print_hello():
    print('hello world=')
output = print_hello()
print(output)

# defualt argument in function

def  multiply(a= 1 , b=2):
    print(" the product is ", a * b )
    return a * b
output = multiply(10, 20)
print(output)
