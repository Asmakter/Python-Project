def addition(a,b):
    print("Sum=",a+b)
def subtraction(a,b):
    print("Subtraction=",a-b)
def multiply(a,b):
    print("Multiplication=",a*b)
def div(a,b):
    print("Division=",a/b)

while True:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Enter Operator like + or - or * or /:   ")

    if op == "+":
        addition(x, y)
    elif op == "-":
        subtraction(x, y)
    elif op == "*":
        multiply(x, y)
    elif op == "/":
        div(x, y)
    else:
        print("Inavalid operator..")

    of = input("If you want to exit, then type 'OFF',, for continue press any key: ")
    if of == "OFF":
        break