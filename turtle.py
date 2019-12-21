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
        

if __name__ == '__main__':

    # bob = turtle.Turtle()
    # draw_polygon(bob, 7, 70)
    # draw_square(bob, 100)
    # print(nested_grade_score(0))
    # print(grade_score(69))
    # print(check_multiple(15))
    print("is_power(10, 2) returns: ", is_power(10, 2))
    print("is_power(27, 3) returns: ", is_power(27, 3))
    print("is_power(1, 1) returns: ", is_power(1, 1))
    print("is_power(10, 1) returns: ", is_power(10, 1))
    print("is_power(3, 3) returns: ", is_power(3, 3))
    print("is_power(32, 2) returns: ", is_power(32, 2))

    
    
    # return_count()