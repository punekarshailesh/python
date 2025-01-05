'''Syntax: 1 . while loop
   
   while condition:
     # loop body

'''

# i =0
# while i<10:
#     print("yes") # --> inside while loop
    
#     i = i + 1    # --> insdie while loop
# print("done")


''' If condition never becomes false then loop 
keeps getting exectuted i.e. infinite loop '''

''' Infinite loop
 while True:
    print("shailesh")
'''

print("Difference between while printing list using while loop and without loops:\n")

# printing elements of the list using while loop
print("list using while loop:")
List  = ['shailesh'  , 333, 33.33  , True , False]

i = 0 
while i<len(List):
    print(List[i])
    i = i+1


# printing list without loops
print("\nlist without loops:")
print(List)


t = ('shailesh' , 33.334343 , 3847474 , True , False , bool , float , int , str)

# printing tuple using loop
print("\ntuples using while loop:")
j = 0 
while j <len(t):
    print(t[j])
    j = j +1

# printing tuples without loops
print("\ntuples without loops:")
print(t)


# Love Babbar questions
n = int(input("Enter range(even no):\n"))
sum = 0
for i in range(1 ,n+1):
    if i%2 == 0:
        sum += i
print("Sum of even number is:",sum)