''' A ggogle interview to add to a given array
    example : [1,3,4,5] -> [1,3,4,6]
    [1,9,9,9] -> [2,0,0,0]
'''


def add_one(given_array):
    # initialize carry to 1
    carry = 1
    # create a new resultant array with the same length as given array
    resultant_array = [0] * len(given_array)
    # loop through given array starting from right
    for i in range(len(given_array) - 1, -1, -1):
        # add current value to carry
        total = given_array[i] + carry
        # if total is 10, reinitialize carry to 1
        if total == 10:
            carry = 1
        # if total is not 10 reinitialize carry to 0
        else:
            carry = 0
        # update index of resultant array
        resultant_array[i] = total % 10
    # if carry is equal to 1
    if carry == 1:
        # create a new resultant array with length greater than given array by 1
        resultant_array = [0] * (len(given_array) + 1)
        resultant_array[0] = 1

    return resultant_array


if __name__ == '__main__':
    print(add_one([1, 2, 9, 9]))
    print(add_one([9, 9, 9]))
    print(add_one([0]))
    print(add_one([1, 2, 4, 5]))
    print(add_one([1, 3, 0, 0]))
