class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __mul__(self, other):
        multiple = (self.numerator * other.numerator) / (self.denominator * other.denominator)
        return multiple

    def __add__(self, other):
        denum1 = self.denominator
        denum2 = other.denominator
        lcm = compute_lcm(denum1, denum2)
        nom1 = (denum1 / lcm) * self.numerator
        nom2 = (denum2 / lcm) * other.numerator
        new_sum = (nom1 + nom2) / lcm
        print(new_sum)

    # def __eq__(self, other):


def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    print(lcm)
    return lcm


if __name__ == '__main__':
    first = Fraction(5, 3)
    second = Fraction(4, 3)
    print(first + second)
