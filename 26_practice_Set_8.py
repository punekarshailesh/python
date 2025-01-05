# practice set 8 ==> completed

# # Q1 . finding greatest of 3 numbers

# def greatestOfThree(a , b , c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c

# a = int(input("Enter first number:\n"))
# b = int(input("Enter 2nd number:\n"))
# c = int(input("Enter 3rd number:\n"))

# print("The greatest of three is:\t",greatestOfThree(a , b , c))


# # Q2. Converting degree celcius to fahrenheit

# def conversion(degree):
#     f = (degree * 1.8) + 32
#     return int(f)

# degree = int(input("Enter celcius value:\n"))
# print("Degree celcius to fahrenheit:",conversion(degree),"^oF")

# # Q3. How do you prevent a python print() function to print new line at the end
# ''' New line can be prevented by end=" "  so that it will print all print statements in single line'''
# print("How",end=" ")
# print("are",end=" ")
# print("you")


# # Q4. recursive function to calculate the sum of the n natural numbers

# def Recursion_Sum_Of_Natural_Number(num):
#     if num == 0 or num == 1:
#         return 1

#     return num + Recursion_Sum_Of_Natural_Number(num - 1)


# num = int(input("Enter a number:\n"))
# result = Recursion_Sum_Of_Natural_Number(num)
# print("Sum of",num,"natural number is =",result)


''' Q5.function to print the star patern by taking n from user
    * * * 
    * *           ----------->  n = 3
    *
'''

#  solution by me


def StarFunc(num):
    for i in range(num):
        for j in range(i, num):
            print("*", end="")
        print()


num = int(input("Enter number of lines you want:\n"))
StarFunc(num)

# solution by harry


def StarPrint(n):
    for i in range(n):
        print("*" * (n-i))


StarPrint(3)

# Q6. inches to cms conversion


def InchesToCms(inch):
    return inch * 2.54


inch = float(input("\nEnter value in inches:\n"))
print("After converting inches to cms:", InchesToCms(inch), "cm")


# Q7. function to remove a given word from a string and strip at the same time
def replace_and_strip(string, word):
    string = string.replace(word, "")
    return string.strip()


string = input("\nEnter string:\n")
print("After removing and using strip() at same time then result:\n",
      replace_and_strip(string, "shailesh"))

# Q8. Function for multiplication table


def mulTable(n):
    print("\nMultiplication table of", n, "is:")
    for i in range(1, 11):
        print(n * i)


n = int(input("Enter a number to get table:\n"))
mulTable(n)
