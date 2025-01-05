

a = 4
b = 5

# 1) Arithmetic operators 
#  ( * , - , / , +)

print("Arithmetic Operators : ")
print ("The value of",a,"+",b ,"is",a+b)
print ("The value of",a,"-",b ,"is",a-b)
print ("The value of",a,"/",b ,"is",(a/b))
print ("The value of",a,"*",b ,"is",a*b)




# 2) Assignment operators
# (= , += , -= , *=  , /= , % .....)

print("\nAssignment Operators : ")
a += 1      # a = a + 1 
print("Value of a : ",a)   # ANS a = 5
a *= 2      # a = a * 2
print("Value of a : ",a)   # ANS a = 10
b /= 3      # b = b / 3
print("Value of b : ",b)   # ANS b = 1.67777.....
b -= 5       # b = b - 5
print("Value of b : ",b)   # ANS b = -3.3333.....


# Floating point number

c = 34
c -= 12
c *= 12
c /= 12
print(c)  # c = 22.0    Why??? ANS if the number is floating point then it gives floating value eg. 33/3 = 11.0 , 44/4 = 11.0



# 3) Comparison Operators
# ( == , > , < , <= , >= , != , ....)

print("\nComparasion Operator : ")
d = 34
e = 32
print("Value of d < e",d<e)
print("Value of d > e",d>e)
print("Value of d <= e",d<=e)
print("Value of d >= e",d>=e)
print("Value of d != e",d!=e)
print("Value of d == e",d==e)

# 4) Logical Operators
# ( and , or , not , ......) 
# These works on boolean values like - true , false

print("\nLogical Operators : ")
bool1 = True
bool2 = False

print("Value of bool1 and bool2 ",bool1 and bool2)
print("Value of bool1 or bool2 ",bool1 or bool2)
print("Value of not(bool1) ",not(bool1))
print("Value of not(bool2) ",not bool2)
