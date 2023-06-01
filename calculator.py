def addition(x,y):
    return x + y

def subrtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def divsion(x,y):
    return x / y

while True:
    print("Select operation:\nAdd\nSubtract\nMultiply\nDivide")
    operation = input("")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation == "Add":
        result = addition(num1,num2)
        print(result)
    elif operation == "Subtract":
        result = subrtraction(num1,num2)
        print(result)
    elif operation == "Multiply":
        result = multiplication(num1,num2)
        print(result)
    elif operation == "Divide":
        result = divsion(num1,num2)
        print(result)
    else:
        print("Not a vaild operation, please choose again.")


