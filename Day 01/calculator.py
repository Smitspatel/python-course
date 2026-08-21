a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
operation = input("select airthmetic operation (+,-,*,/,%,**)")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/" and b !=0:
    print(a / b)
elif operation == "%" and b !=0:
    print(a % b)
elif operation == "**":
    print(a ** b)
else:
    print("Invalid operation")
# find error in below code
name = input("Enter your name: ")
age = int(input("Enter your age: ")) # this taken as string so condition not check , we have to convert into int

if age >= 18:
    print(name, "is an adult")
else:
    print(name, "is a minor")

# range 
nums = range(8)  # range is [0,1,2,3,4,5,6,7]
print(nums)
newRange = range(1,15)  # rnage start from 1 and end at 15 range(start,stop,step) range(1,50,2) step means ketla plus krva next ma ae 
print(newRange)

#loops (repeat work )
i = 1
while i <= 4:
    print(i)
    i += 1
print("end of code")

# for loop (majority programmar use this loop)
nums = range(6)
for i in nums:
    print(i)
for i in range(1,10,2):
    print(i)

for i in range(1,51):
    if(i % 3 == 0):
        print(i)
    if(i == 30):
        break
print("out of loop")

#practice 
for i in range(1,21,2):
    print(i)

for i in range(1,51):  #skip 15
    if(i == 15):
        continue
    if(i % 3 == 0):
        print(i)

#list
marks = [99,85,74,84.50,80,"A"]   #collection of items we can use float , int, str 
print(marks, type(marks), len(marks))

#index 0 to start 
print(marks[1])
print(marks[-1]) # last side first 

#slicing a list (some portion seperate) list[start:end]
print(marks[0:4])
print(marks[-3:])

for score in marks:
    print(score)

# list are mutable , we can add or remove from that 
marks.append(50)
marks.insert(2, 75)
print(marks)
print(50 in marks)
print(100 in marks)

#tuple are immutable 
marks = (99,85,74,84.50,80,"A")
print(marks , type(marks))

#set => unique items collection
marks = {99,85,74,99,84,80,85}
print(len(marks))

#dictonary is collection of key=>value pair 
marks = {"Maths": 91, "Physis": 58, "Chemistry":89}

#function

def sum(a,b):
    print(a+b)
print(sum(1,2))