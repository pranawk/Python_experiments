def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
       return "Error, divided by zero"
    return a/b
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operations={
 '1': add,
 '2': sub,
 '3': multiply,
 '4': divide
}
choice= input("Enter choice (1/2/3/4):")

if choice in operations:
    num1= float(input("Enter first number:"))
    num2= float(input("Enter second number:"))

    result= operations[choice](num1,num2)
    print("Result:",result)
else:
    print("Invalid input")
