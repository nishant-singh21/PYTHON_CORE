#lambda function 
# when we use when we write an quick function and we don't want to give it a name 
#   lambda args: expression 


# add = lambda x, y: x + y 
# print(add(5, 10))

# def add_func(x, y):
#     return x + y
# print(add_func(5, 10))



# nums = [1, 2, 3, 4, 5]
# # squared = list(map(function , iteration))

# squared = list(map(lambda x: x**2, nums))
# print(squared)

# # lambda function with filter
# nums = [1, 2, 3, 4, 5]  
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  # Output: [2, 4]


# lambda function with reduce


from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120
