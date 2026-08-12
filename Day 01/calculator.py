a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
operation = input("select airthmetic operation (+,-,*,/,%,**)")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
elif operation == "%":
    print(a % b)
else:
    print(a**b)
# find error in below code
name = input("Enter your name: ")
age = input("Enter your age: ") # this taken as string so condition not check , we have to convert into int

if age >= 18:
    print(name, "is an adult")
else:
    print(name, "is a minor")
