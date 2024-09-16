import cases
print(cases.show())

#define a new module in this new module as a user defined function
def hello():
    print("It is monday today")
hello()

#wap using the inbuild calculator module & perform addition, substraction, multiplication of two numbers:
# import Calculator
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# print(num1 + num2)

#Wap for performing different arithmetic performance call func def -> add, sub, mul, divide save this program as c
# import Calculator
def Add(a,b):
    return a+b
def Mul(a, b):
    return a *b
def Sub(a,b):
    return a - b
def div(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b

# print(add(5,7))
# print(mul(4,3))
# add(5,9)
# mul(5,6)
# sub(9,5)
# div(4,12)
