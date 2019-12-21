# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
        
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
        
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag

# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag

# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True

import math
def my_sqrt(a):
    x = 3
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            return y
            break
        x = y 

def test_sqrt():
    for index in range(1, 26):
        my_soln = my_sqrt(index)
        py_soln = math.sqrt(index)
        diff = my_soln - py_soln
        print(f'a = {index} | my_sqrt({index}) = {my_soln} | math.sqrt({index}) = {py_soln} | diff = {diff}')
if __name__ == "__main__":
    # print(any_lowercase1('CALory'))
    # print(any_lowercase2('fish'))
    print(test_sqrt())