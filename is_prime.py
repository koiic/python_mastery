
# def is_divisible(a,b):
#     """ Function to check if number is divisible"""
    
#     if b == 0 or b == 1: # check if b is equal to 0 or 1
#         return False
    
#     if a <=1 or a < b: # lesser number isn't a power of a greater number
#         return False
#     if a % b == 0:
#         return True
#     return False

# def is_power(a, b):
#     """ Function to check if a number is a power of the other"""
#     if is_divisible(a, b) and is_power(a/b, b):
#         return True
#     return False


def hypotenuse(sideA, sideB):
    # sideC = sideA**2 + sideB**2
    # print(sideC)
    import math
    side_a_squared = sideA**2 
    side_b_squared = sideB**2
    side_c_squared = side_a_squared + side_b_squared
    print (math.sqrt(side_c_squared))    
    return 0

if __name__ == '__main__':
    # print("is_power(10, 2) returns: ", is_power(10, 2))
    # print("is_power(27, 3) returns: ", is_power(27, 3))
    # print("is_power(1, 1) returns: ", is_power(1, 1))
    # print("is_power(10, 1) returns: ", is_power(10, 1))
    # print("is_power(3, 3) returns: ", is_power(3, 3))
    # print("is_power(32, 2) returns: ", is_power(32, 2))
    print(hypotenuse(10, 20))
