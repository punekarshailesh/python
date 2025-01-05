'''
         Range function in python:
         -> used to generater sequence of numbers
         -> range(start , stop , step_size) 
        '''


# 1. range(start , stop)

# printing numberse from 0 to 9
print("Numbers from 0 to 9:")
for i in range(0 , 10):
    print(i)

# printing numbers from 1 to 8
print("\nNumbers from 1 to 8:")
for num in range(1 , 9):
    print(num)


# priting numbers from 1 to 100
print("\nNumbers from 1 to 100:")
for r in range(1 , 101):
    print(r)


# Using range(start , stop , step_size) 
# step_size represents kitne value skip karega
# rarely we use step_size
print("\nPrinting numbers by skip value of 2:")
for i in range(1 , 10 , 2):
    print(i)


# i = 1
# while i in range(0 , 10): # --> forms the infinite loop and prints 1 inifnite times
#     print(i)