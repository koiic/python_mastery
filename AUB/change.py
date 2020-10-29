

"""
1. Make change.
Write a function make_change() that takes in an integer n (number of Lebanese pounds in thousands) and prints out the best way (fewest number of bills) to make change using 100, 50, 20, 10, 5 and one thousand bills.
 The algorithm for producing the smallest number of bills will dispense as many bills of 100 thousands as possible, then 50 thousands, then 20 thousands, then 10 thousands, then 5 thousands, and finally one thousand.
The function should return a list of tuples, where each tuple is a pair consisting of a denomination and a (non-zero) number of bills of that denomination.
For example, make_change(92) returns [(50, 1), (20, 2), (1, 2)].

"""

def get_denom(amount, arr):
    temp = []
    for i in range(len(arr)):
        if amount > arr[i]:
            temp.extend(arr[i:])
            break
    return temp

denomination = [100, 50, 20, 10, 5, 1]


def make_change(amount):
    amount_list = []

    temp = get_denom(amount, denomination)
    for i in range(len(temp)):
        value, divisor, mod = change(amount, temp[i])
        amount_list.append((value, divisor))
        amount = mod
    return amount_list


def change(new_amount, divisor):
    if new_amount == divisor:
        return divisor, 1, new_amount
    elif new_amount > divisor:
        div, mod = divmod(new_amount, divisor)
        return divisor, div, mod
    else:
        return divisor, 0, new_amount


def print_change(amount):
    denom_dict = {
        100: "100,000",
        50: "50,000",
        20: "20,000",
        10: "10,000",
        5: "5,000",
        1: "1,000"
    }
    change = make_change(amount)
    print(change)
    for cash in change:
        if cash[1] != 0:
            print("LBP", denom_dict[cash[0]])
    # print(change)

if __name__ == '__main__':
    print(print_change(92))
