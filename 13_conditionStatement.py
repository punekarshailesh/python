''' Conditional statements
'''

# if-else

age = int(input("Enter age : "))

if (age >= 18):
    print("eligible to vote")
else:
    print("Not eligible")



print()


# if-elif-else => ladder

a = int(input("Enter 1st number:\n"))
b = int(input("Enter 2nd number:\n"))

if (a > b):
    print("a is greater than b")
elif(a == b):
    print("a is equal to b")
else:
    print("b is greater than a")


''' 
Relational Operator : == , <= , >= , < , >
Logical Operator : and , or , not
'''

# office work eg.

# 1. and Operator
emp_age = int(input("Enter your age:\n"))

if(emp_age > 18 and emp_age <=50):
 print("You can work for ABC company!")
else:
    print("You are not eligible!")

# or Operator
if emp_age > 18 or emp_age <50:
 print("You can work")
else:
    print("You can not work")



# Is else OPTIONAL?
age = 9
if age ==7 :
    print("YES")
elif age > 34:
    print("NO")
else:
    print("Yes , else is optional")



# CodeHelp Babbar

c = input("Enter character:")

if c>='a' and c<='z':
    print("Lower case")
elif c>='A' and c<='Z':
    print("Upper case")
elif c>='0' and c<='9':
    print("Numeric value")
else:
    print("Special character")

