#Functions
#Declaring a function
def generate_full_name ():
    first_name = 'Ayesha'
    last_name = 'Ali'
    space = ' '
    full_name = first_name + space + last_name
    print("Full name:",full_name)
generate_full_name()
#declaring a function of addition
def adding_numbers():
    num_one = 5
    num_two = 4
    total = num_one + num_two
    print("Total:",total)
adding_numbers()
#Function returning a value
def adding_two_numbers():
    num_one = 6
    num_two = 35
    total = num_one + num_two
    return total
print("Total:",adding_two_numbers())
#Function with one parameter
def greetings(name):
    message = name + ",Welcome to learning Python"
    return message
print("Greetings:",greetings("Izza Iftikhar"))
#adding numbers
def add_numbers(number):
    num = 50
    total = number + num
    return total
print("Total:",add_numbers(50))
#declaring square of numbers
def square(x):
    square = x * x
    return square
print("Square:",square(4))
#declaring area of circle
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
print("Area of circle:",area_of_circle(5))
#Function with two parametes
#declaring first and last name
def generate_full_name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print("Full name:",generate_full_name('Izza','Iftikhar'))
#declaring age 
def age(birth_year,current_year):
    age = current_year - birth_year
    return age
print("Age:",age(2007,2026))
#Passing Arguments with Key and Value
def subject_name(sub_one,sub_two):
    space = ' '
    subject_name = sub_one + space + sub_two
    return subject_name
print("Subjects:",subject_name(sub_one = 'English', sub_two = 'Math'))
#Returning a string
def name(first_name):
    return first_name
print("Name:",name("Izza Iftikhar"))
#Returning a number
def numbers(num_one,num_two):
    total = num_one + num_two
    return total
print("Sum of numbers:",numbers(18,20))
#Returning a boolean
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print("Even:",is_even(5))
print("Even:",is_even(8))
#Returning a list
def take_fruits():
    fruits = ['Apple','Mango','Banana']
    return fruits
print("Fruits:",take_fruits())
#Function with Default Parameters
#declaring greeting 
def greetings(name = 'Ali'):
    message = name + ", Welcome! to functions inside python."
    return message
print("Greetings:",greetings())
print("Greetings:",greetings('Izza'))
#declaring name
def generate_full_name(first_name = 'Ayesha', last_name = 'Ali'):
    space = " "
    full_name = first_name + space + last_name
    return full_name
print("Full name:",generate_full_name())
print("Full name:",generate_full_name('Ali','Akbar'))
#Arbitrary Number of Arguments
def sum_of_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_numbers(4,7,13))
#Default & Arbitrary Number of Parameters in Functions
def generate_groups(team,*args):
    print(team)
    for  i in args:
        print(i)
print(generate_groups('Team-1','Ali','Akbar','Ayesha'))
#Function as a Parameter of Another Function
def square_number(n):
    return n * n
def do_something(f,x):
    return f(x)
print(do_something(square_number,5))

#Exercise
#Exercises: Level 1
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_one,num_two):
    total = num_one + num_two
    return total
print(add_two_numbers(4,5))

#Area of a circle is calculated as : area = π x r x r. Write a function that calculates area_of_circle
def area_of_circle(r):
    π = 3.14
    area = π * r * r
    return area
print(area_of_circle(13))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*numbers): 
    total = 0
    for num in numbers:
         total += num
    return total
print(add_all_nums(2,3,4,5))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.capitalize()
    if month in ['December','January','February']:
        return 'Winter'
    elif month in ['March','April','May']:
        return 'Spring'
    elif month in ['June','July','August']:
        return 'Summer'
    elif month in ['September','October','November']:
        return 'Autumn'
    else:
        return 'Invalid month'
print(check_season('May'))

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'Slope is unidentified'
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(4,7,3,9))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(fruits):
    for fruit in fruits:
      print(fruit)
print(print_list(['Apple','Banana','Mango']))

#Write a function named calculate_sum() that takes two parameters,returns their sum
#Ask the user to enter two numbers using input(), call the function, and print the result.
num_one = int(input("Enter a number:"))
num_two = int(input("Enter a number:"))
def calculate_sum(num1,num2):
    total = num1 + num2
    return(total)
print(calculate_sum(num_one,num_two))

#Take 2 parameters,return their product.Then ask the user for two numbers and print the answer.
prod_1 = int(input("Enter a number:"))
prod_2 = int(input("Enter a number:"))
def multiply(a,b):
    product = a * b
    return product
print(multiply(prod_1,prod_2))

#Write a function named find_smallest(a, b) that takes 2 parameters,returns the smaller number
#Then:Ask the user for two numbers.Call the function.Print the result
n_1 =int(input("Enter a number:"))
n_2 =int(input("Enter a number:"))
def find_smallest(a,b):
    if a > b:
        return b
    return a
print(find_smallest(n_1,n_2)) 

#Write a function named is_positive(number) that takes one parameter
#returns "Positive" if the number is greater than 0,otherwise returns "Not Positive"
#Ask the user for a number and print the returned result
num = int(input("Enter a number:"))
def is_positive(number):
    if number > 0:
        return 'Positive'
    return 'Not Positive'
print(is_positive(num))

#Write a function named greet_user() that has one parameter name and default parameter message="Welcome!"
#prints both the name and the message,Call the function twice:Only pass the name "Izza",Pass both "Ali" and "Good Morning!"
def greet_user(name,message = 'Welcome'):
    greetings = 'Hello! ' + name + " " + message
    return greetings
print(greet_user('Izza'))
print(greet_user('Ali','Good Morning'))

#Write a function named find_average() that takes list of numbers as parameter,returns the average of all numbers in list and print
def find_average(lst):
    lst_num = [10, 20, 30, 40, 50]
    average = sum(lst_num) / 5
    return average
print(find_average(average))

#Write a function named count_even() that takes a list of numbers as a parameter,returns how many even numbers are in the list
list_one = [2, 5, 8, 11, 14, 17, 20]
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count
print(count_even(list_one))