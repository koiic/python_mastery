import math

def my_sqrt(a):
    """
    Method to find the square root of number
    using the newtons formula
    value = (x + a/x) / 2.0
    """
    x = 3
    while True:
        y = (x + a/x) / 2.0           # find the value of y using the formula
        if y == x:                    # check if y is equal to x
            return y
        x = y                         # if x not equal y assign x to the value of y

def test_sqrt():
    """
        This method is to test the diffence between the value of 
        the function my_sqrt() and the builtin square root function (math.sqrt())
    """
    
    for index in range(1, 26): # get value from 1-25
        my_soln = my_sqrt(index) # return value from my_sqrt function
        
        py_soln = math.sqrt(index) # return value from math.sqrt function
        
        diff = my_soln - py_soln # difference between the two function
        
        print(f'a = {index} |  my_sqrt({index}) = {my_soln} |  math.sqrt({index}) = {py_soln} |  diff = {diff}')
        
        
        
        
def modified_function():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter in ['O', 'Q']:
            print(letter + 'u' + suffix)
        else :
            print(letter  + suffix)


#Write a Python program to remove the characters which have odd index values of a given string
def remove_odd_index(word):
    statement = ""
    for i in range(len(word)):
        if i % 2 != 0:
            statement += word[i]
    return statement


def reverse_string(word):
    reverse = ""
    for char in word:
        reverse = char + reverse
    return reverse
    

def check_palindrome(word):
    reverse = reverse_string(word)
    if reverse.lower() == word.lower():
        return True
    return False


if __name__ == "__main__":
    print(modified_function())
    print(remove_odd_index('CALORY'))
    print(reverse_string('CALORY'))
    print(check_palindrome('balnKet'))