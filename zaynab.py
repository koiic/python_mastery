


def add_number(x, y):
    return x + y

def substract_number(x, y):
    return x - y

def start_point():
    print("enter 1 for addition")
    print("enter 2 our substraction")
    print("enter 3 to end \n")
    value = int(input("enter your choice :  "))
    if value == 3:
        exit()
    elif value not in [1,2,3]:
        print("=========you've entered an invalid choice===============\n")
        start_point()
    else:
        a = int(input("enter first digit: "))
        b = int(input("enter second digit: "))
        if value == 1:
            return add_number(a,b)
        elif value == 2:
            return substract_number(a, b)

if __name__ == "__main__":
    print(" =========================welcome to main calculator=======================================\n") 
    try:
        while True:
            print("your answer is : ", start_point())
            print("================================================\n")
            print("do you want to continue")

    except KeyboardInterrupt:
        exit()

  