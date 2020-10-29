"""
3. Trig Table.
Write a function trig(first, last, increment) that prints the sin and cos of angles θ, first ≤ θ ≤ last, in increments increment.
 The integers θ values should be formatted with 4 slots and left justified, and the floats sin and cos values should be
formatted with 10 slots, with 5 after the decimal point. For example, the call trig(0, 180, 45) should print:

"""
import math


def trig(first, last, increment):
    my_array = []
    while first != last:
        my_array.append(get_sin_cos(first))
        first += increment
    return my_array

def get_sin_cos(angle):
    # sin = math.sin(angle)
    sin = "{:.5f}".format(math.sin(angle))
    cos = "{:.5f}".format(math.cos(angle))
    return angle, sin, cos

if __name__ == '__main__':
    print(trig(0, 180, 45))