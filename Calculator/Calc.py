print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

c = 1
while c == 1:
    def divide(x,y):
        if y == 0:
            return "The value Cannot divide by zero"
        return f"The Answer is {x/y}"
    first_number = int(input("Enter First Number is: "))
    second_number = int(input("Enter Second Number is: "))
    i = int(input("Enter the operator: "))

    if i == 1:
        print(f"The Answer is {first_number + second_number} ")
    elif i == 2:
        print(f"The Answer is {first_number - second_number} ")
    elif i == 3:
        print(f"The Answer is {first_number * second_number} ")
    elif i == 4:
        print(divide(first_number,second_number))
    else:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("         Press Valid Operator")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Enter 1 to continue")
    print("Enter 0 to exit")
    c = int(input())
