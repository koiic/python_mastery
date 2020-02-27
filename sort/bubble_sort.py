def bubble_sort(array):

    arr_len = len(array)
    #[4,6,3,7,0]
    for index in range(arr_len):
        for j in range(0, arr_len-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


    return array


if __name__ == '__main__':
    print(bubble_sort([31,41,59,26,41,58]))
