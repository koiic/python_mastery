''' Using turtle to draw diagrams and shape'''

# import turtle
# import math

# def draw_square(obj, length):
#     for i in range(4):
#         obj.fd(length)
#         obj.lt(90)


# def draw_polygon(obj, sides, length):
#     angle = 360/sides
#     for i in range(sides):
#         obj.fd(length)
#         obj.lt(angle)

# def draw_circle(obj, radius):
#     circumference = 2 * math.pi * radius
#     n = 50
#     length = circumference / n
#     draw_polygon(obj, n, length)
    
    
def grade_score(score):
    print(score)
    if score >= 70:
        return f'Grade for score {score} is A'
    elif score > 65 <= 69:
        return f'Grade for score {score} is B'
    elif score > 55 <= 65:
        return f'Grade for score {score} is C'
    elif score > 45 <= 55:
        return f'Grade for score {score} is D'
    elif score >= 40 <= 45:
        return f'Grade for score {score} is E'
    else:
        return f'Grade for score {score} is F'


# def nested_grade_score(score):
#     """ Function to check if score is Even, Odd or a Neutral value """
#     if score == 0 :
#         return 'score is Neutral'
#     else:
#         if score % 2 == 0:
#             return 'score is Even'
#         else:
#             return 'score is Odd'
        
# def check_multiple(number):
#     """ Function to check if positive number is a multiple of 3 and 5"""
#     if number < 0:
#         return 'Invalid number'
    
#     else:
#         if number % 2 == 0:
#             return 'Not a multiple of 3 or 5'
#         else:
#             if number % 3 == 0 and number % 5 == 0:
#                 return 'Hurray, number is a multiple of 3 and 5'
#             else:
#                 if number % 3 == 0:
#                     return 'number is a multiple of 3'
#                 elif number % 5 == 0:
#                     return 'number is a multiple of 5'
#                 else:
#                     return 'Not a multiple'
                    
                    
def check_multiple_refactor(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'Hurray, number is a multiple of 3 and 5'
    elif number % 3 == 0:
        return 'number is a multiple of 3'
    elif number % 5 == 0:
        return 'number is a multiple of 5'
    else:
        return 'not a multiple of 3 or 5'

# def countup(n):
#     if n >= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countup(n + 1)
    
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
                       
# def return_count():
#     user_input = int(input('Enter number : '))
#     if user_input > 0:
#         countdown(user_input)
#     else:
#         countup(user_input)

# def print_summation(number):
    
#     value = '2'
#     print(number + int(value))

# def recurse(a):
#     if (a == 0):
#         print(a)
#     else:
#         recurse(a)

#A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
#function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
#you will have to think about the base case

def is_divisible(a,b):
    """ Function to check if number is divisible"""
    
    if b == 0 or b == 1: # check if b is equal to 0 or 1
        return False
    
    if a <=1 or a < b: # lesser number isn't a power of a greater number
        return False
    if a % b == 0:
        return True
    return False

def is_power(a, b):
    """ Function to check if a number is a power of the other"""
    if is_divisible(a, b) and is_power(a/b, b):
        return True
    return False



# def is_power(a,b):
# #'''this program checks if number1 is a power of number2'''

#     if (a<b):  # lesser number isn't a power of a greater number
#         return False
#     elif (b==0) or (b==1) : # Exception cases
#         return False
#     elif a%b == 0 and is_power(a/b, b) == True:  # Condition check for is_power (Recursion!)
#         return True
#     else:
#         return False

def modify_list(sequence):
    for value in sequence:
        if value % 2 == 0:
            print('====', value)
            sequence.remove(value)
    return sequence

"""
Part 1

Write a Python program that does the following. 

Create a string that is a long series of words separated by spaces. The string is your own creative choice. It can be names, favorite foods, animals, anything. Just make it up yourself. Do not copy the string from another source. 

Turn the string into a list of words using split. 

Delete three words from the list, but delete each one using a different kind of Python operation. 

Sort the list. 

Add new words to the list (three or more) using three different kinds of Python operation. 

Turn the list of words back into a single string using join. 

Print the string. 

Part 2

Provide your own examples of the following using Python lists. Create your own examples. Do not copy them from another source. 

Nested lists 
The “*” operator 
List slices 
The “+=” operator 
A list filter 
A list operation that is legal but does the "wrong" thing, not what the programmer expects 
Provide the Python code and output for your program and all your examples. 
"""
        
# def stringify():
#     my_string = "my tough decision as a college student"
#     string_list = my_string.split(" ") # split string with spaces, convert the sting to a list
#     string_list.pop(0) # pop item on index 4 --> returns the popped value
#     del string_list[2] # delete item on index 1
#     string_list.remove("decision") # remove item in array by value
#     string_list.sort() # sort list alphabetically
#     # #add item to list
#     string_list.append("as") # append a new item to list
#     string_list.insert(1, "great") # insert an item in the specified index
#     string_list.extend(("strong", "lion")) # add an iterable to the list
    
#     new_string = " ".join(string_list) # join item in list to revert back to string
    
#     return new_string
    


# def my_nested_list_example():
#     # this function create a nested list
#     new_list = [[item*2 for item in range(4) ] for i in range(5) ]
#     return new_list 
    
# #the * operator is used to create multiple version of a list
# def multiple_list_value():
#     #funvtion to multiply list value
#     return my_nested_list_example() * 2


# def list_filter_example():
#     #filter list to return string greater than 4
#     list_of_food = ["rice", "spaghetti", "beans", "coconut", "strawberry"]
#     new_food = list(filter(lambda value: len(value) > 4, list_of_food))
#     return new_food


# def join_item_in_list():
#     # joining item in python using the (+=) operator
#     my_list = []
#     my_list += ["fish", "rice", "bat"]
    
#     return my_list


# def list_slice():
#     # python slice implementation
#      list_of_food = ["rice", "spaghetti", "beans", "coconut", "strawberry"]
#      slice_object = slice(1, 4)
#      return  list_of_food[slice_object]
 
# def return_even_numbers():
#     # function to reurn even numbers within 1 - 10
#     even_numbers =  [value for value in range(10) if value % 2 == 1 ]
#     return even_numbers

if __name__ == '__main__':

    # bob = turtle.Turtle()
    # draw_polygon(bob, 7, 70)
    # draw_square(bob, 100)
    # print(nested_grade_score(0))
    # print(grade_score(69))
    # # print(check_multiple(15))
    # print("is_power(10, 2) returns: ", is_power(10, 2))
    # print("is_power(27, 3) returns: ", is_power(27, 3))
    # print("is_power(1, 1) returns: ", is_power(1, 1))
    # print("is_power(10, 1) returns: ", is_power(10, 1))
    # print("is_power(3, 3) returns: ", is_power(3, 3))
    # print("modified list ", modify_list([9,8,7,6,5,4,3,2]))
    # print("modified string::::  ", stringify())
    # print("nested list::::  ", my_nested_list_example())
    # print("multiple list::::  ", multiple_list_value())
    # print("list slice::::  ", list_slice())
    # print("joined list::::  ", join_item_in_list())
    # print("filtered list::::  ", list_filter_example())
    # print("even list::::  ", return_even_numbers())



    
    
    # return_count()