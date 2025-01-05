def greet(name_user):
    print("Good day ,"+ name_user)


name_user = input("Enter name of user:\n")

print("Without loop:")
greet(name_user)    # ->printing one time


''' 
    calling function greet() 10 times 
         so output will print
             Good day sir - 10 times on console 
   
'''
print("\nUsing for loop:")
for i in range(10):
    greet(name_user)



# functions with arguments

def add(a , b):
    return (a+b)

print("\nSum using add function:",add(5,6))


def sub(a , b , c , d):
    return (a-b-c-d)

print("\nSubstraction using sub():",sub(4,4,4,4))

def mul(a , b):
    return a*b

print("\nMultiplication using mul():",mul(5 , 6))
