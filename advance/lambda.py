def myfunc(n):
    print('this is n', n)
    return lambda x: x * n


if __name__ == '__main__':
    doubler = myfunc(2)
    print(doubler(6))

    ### Custom sorting using a lambda function as key parameter
    points2d = [(1, 9), (4, 1), (5, -3), (10, 2)]
    sorted_by_y = sorted(points2d, key=lambda x: x[1])
    print(sorted_by_y)

    my_list = [-1, -4, -2, -3, 1, 2, 3, 4]
    sorted_by_abs = sorted(my_list, key=lambda x: abs(x))
    print(sorted_by_abs)

    ###use lambda for map function
    a = [1, 2, 3, 4, 5, 66, 7]
    b = list(map(lambda x: x * 2, a))
    print(b)
