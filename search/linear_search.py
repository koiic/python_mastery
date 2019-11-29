'''
Consider the searching problem:
Input: A sequence of n numbers A D ha1;a2;:::;ani and a value 􏰁.
Output: An index i such that 􏰁 D AŒi􏰀 or the special value NIL if 􏰁 does not
appear in A.
'''

# pseudocode
'''
    A = list
    V = number
    for j = 1 --> A.length
        key = A[j]
        if key == number:
            return j
        return Nil

'''


def search(array, number):
    for index in range(1, len(array)):
        if array[index] == number:
            return index
    return None
    

'''
Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. 
The sum of the two integers should be stored in binary form in an (n + 1) element array C . 
State the problem formally and write pseudocode for adding the two integers.
'''
# pseudocode
'''
    A = n-binary list
    B = n-binary list
    C = A' + B'
    for index = 1 --> A.length
        carry = 0
        summation = A[index] + B[index] + carry
        add value of summation % 2 -> c
        carry = floor division(s/2)
    append carry to c

'''

def add_binary_integers(first_list, second_list):
    c = []
    carry_over = 0

    for index in range(len(first_list)-1, -1, -1):
        summation = first_list[index] + second_list[index] + carry_over
        print(summation)
        c.append(summation % 2)
        carry_over = summation // 2
    c.append(carry_over)
    return c[::-1]



'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''


def is_pangram(s):
    import string

    set_string = set(list(s.lower()))
  # print(set_string)
    alpha = set(list(string.ascii_lowercase))
    intersect = list(set_string.intersection(alpha))
    for i in list(alpha):
        if i not in intersect:
            return False
    return True


''' Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.'''

def unique_in_order(iterable):
  unique_list = []
  if len(iterable) == 1:
    unique_list.append(iterable)
  for index in range(0, len(iterable)):
    if iterable[index] != iterable[index - 1]:
    # if iterable[index] not in unique_list:
      unique_list.append(iterable[index])
    
    if iterable[index] not in unique_list:
      unique_list.append(iterable[index])
   
  return unique_list


print(unique_in_order('AAABBBCCc'))



if __name__ == '__main__':
    print(search([31,41,59,26,41,58], 26))
    print(search([31,41,59,26,41,58], 1))
    print(add_binary_integers([0,0,0,], [1,1,1]))
    print(is_pangram("The quick brown fox jumps over the lazy dog" ))




