# pseudocode

'''
    for j = 2 --> A.length
        key = A[j]
        i = j-1

        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
'''

# implementation

def insertion_sort(array):

    for index in range(1, len(array)):
        key = array[index]
        
        previous_index = index - 1

        while previous_index >= 0 and array[previous_index] > key :
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1
        array[previous_index + 1] = key
   
    return array


def insertion_sort_non_decreasing(array):

    for index in range(1, len(array)):
        key = array[index]
        
        previous_index = index - 1

        while previous_index >= 0 and array[previous_index] < key :
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1
        array[previous_index + 1] = key
   
    return array


if __name__ == '__main__':
    print(insertion_sort([31,41,59,26,41,58]))
    print(insertion_sort_non_decreasing([31,41,59,26,41,58]))


