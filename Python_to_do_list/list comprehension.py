# List Comprehension
#Changing a string to a list of characters
language = 'Python'
lst = [i for i in language]
print(lst)
print(type(lst))
print(len(lst))
#Generating a list of numbers
#Generating numbers
num = [i for i in range(11)]
print(num)
#Generating square
square = [i * i for i in range(9)]
print(square)
#Generating list of tuples
tuple = [(i,i * i) for i in range(1,8)]
print(tuple)
#Generating even numbers
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)
#Generating odd numbers
odd_numbers = [i for i in range(20) if i % 2 ==1]
print(odd_numbers)
#Filter numbers
numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
filter_number = [i for i in numbers if i % 2 == 0 ] 
print(filter_number)
#Flattening a three dimensional array
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattening_lists = [numbers for rows in list_of_lists for numbers in rows]
print(flattening_lists)

#Lambda function
#Adding numbers
add_numbers = lambda a,b : a + b
print(add_numbers(1,2))
#Taking square
square_numbers = lambda a : a * a
print(square_numbers(4))
#Taking cube
cube_numbers = lambda b : b ** 3
print(cube_numbers(5))
#Taking multiple variables
numbers = lambda a, b, c, d : a ** 2 + b * 4 - 2 * c / 4 * d
print(numbers(1,2,3,4))
#Checking even numbers
even_numbers = lambda a : a % 2 == 0
print(even_numbers(6))
print(even_numbers(3))
#Lambda Function Inside Another Function
def num(a):
    return lambda n : a ** n
square = num (3)(4)
print(square)
cube = num(5)(3)
print(cube)
#Adding two numbers 
def num(b):
    return lambda n: b + n
add = num(3)(3)
print(add)

#List Comprehensions Exercises
#Filter only negative and zero in the list using list comprehension 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_numbers = [i for i in numbers if i <= 0 ]
print("Filter numbers:",filter_numbers)

#Flatten the following list of lists of lists to a one dimensional list 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattening_lists = [numbers for rows in list_of_lists for rows in rows for numbers in rows]
print("Flattening lists:",flattening_lists)

#Using list comprehension create the following list of tuples:
num_tpl = [(i,1,i,i ** 2,i ** 3,i ** 4,i ** 5)for i in range(0,11)]
for items in num_tpl:
    print("List of tuples:",items)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
calculate_slope = lambda x1,y1,x2,y2 : (y2 - y1) / (x2 - x1)
print("Slope:",calculate_slope(2,5,4,8))
y_intercept = lambda x,y,m : y - (m * x)
print("y-intercept:",y_intercept(3,5,8))

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list = [f"{first}{last}" for name in names for first, last in names]
print(names_list)
#Change the following list to a list of dictionaries:countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
