
'''
   Input function always takes input as a string
   if we are dealing with numbers just typecast it to an integer
   input() ==> Always takes input as string
'''

a = input()
print("Type of a : " ,type(a) )
print("Value of a : ",a)

b = input("\nEnter a number : ") 
b = int(b)  # Typecasting only possible when string letters are digits otherwise no chance to typecast
print("Value of b : ",b)

y = input("Enter string:")
print(y)