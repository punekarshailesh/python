'''
primary Datatypes in python
1. Integer 
2. Float
3. String
4. Boolean
5. None

python - automatically detects the type of a variable
'''

# Integer
a = 383774743
print(a)

# String
h = 'shailesh'
b = "hello world"
c = """madne"""
d = '''NIT Calicut 
is having its diamond jubliee'''
print(h)
print(b)
print(c)
print(d)

# Float
m = 39374.94746464
print(m)



# Booleans --> True ya fir False
p = True
q = False
print(p)
print(q)

print("\nValue of bool(0):",bool(0)) # --> prints - False
print("Value of bool(1):",bool(1)) # --> prints - True
print()

# None 
''' 
   -> Useful in function when function return nothing it actually returns None
'''
r = None
print(r)



# type()

# Printing the type of variables in python
# type() - This function is used to find the type of a variable
print("Type of a  : ", type(a))
print("Type of b : ",type(b))
print("Type of c : ",type(c))
print("Type of d : ",type(d))
print("Type of h : ",type(h))
print("Type of m : ",type(m))
print("Type of p and q : ",type(p) , type(q))
print("Type of r : ",type(r))



''' Rules for variables '''

# 1a = 3   ==> error
# 1_a = 35   --> error
g_ = 9374.33
print("g_ : " , g_)

a_1 = 34
print("a_1 : " ,a_1)

_a = 339.4847
print("_a : ",_a)

# a_@ = 3.33 --> error

# a__/ = "abcd" , a/ ,   --> error

one8 = '''llslsl'''
print("\nUsing ''' This quotes ''' ",one8)


# Case sensitive --> Case sensitivity present in python
a = 3.4
A = 39384
print("a : ",a)
print("A : ", A)


# Typecasting - Changing the one datatype to another datatype
# eg. int -> float , int -> string , float -> int

print("\nTypeCasting : ")
e = 33.44
print("Value of e before typecasting : ",e)
e = int(e)
print("Value of e after typecasting : ",e)
# hey = 'shailesh' --> ERROR
hey = '345'  # --> type of hey is string

print("Original type of hey variable : ",type(hey)) # --> type of hey is str

hey = float(hey)
print("typecasted type of hey variable : ",type(hey))

a1 = 3333
print("a1 type : ",type(a1))
print("Before a1 typecasted value : ",a1) # -> this step is not actually converting int a1 to float a1 the type of a1 is still int

a1 = float(a1) # Now the a1 is actually converted to float datatype actual typecasting
print("a1 type : ",type(a1))
print("After typecasting a1 value : ",a1)  


# Complex

x = complex(1j)
print(type(x))


# power values
x = 35e3
print(type(x) , x)

y = 12E4
print(type(y) , y)

z = -86.7e100
print(type(z) , z)

a = 3 + 2j
print(type(a) , a)

b = -5j
print(type(b) , b)

# typecasting
c = int(x)  # converting complex to int possible
print(c)

# d = int(a)   # Error - converting complex to int NOT possible

comp = complex(y)
print("Type : ",type(comp) , "Value : ",comp)

import random
print(random.randrange(1 , 100))


''' possible Typecastings
   1. int -> float and vice versa
   2. int -> string and vice versa (if possible)
   3. float -> string and vice versa (if possible)
   4. int -> complex but complex -> int (not possible)
   5. float -> complex but complex -> float (not possible)
   6. string -> complex and vice versa
'''
# Typecasting
x = 1   
y = 1.1
z = '353'
a = 2 + 2j
# x = float(x)          # int   -->   float 
# y = str(y)            # float -->   string 
# z = int(z)            # string -->  int 
# z = float(z)          # string -->  float 
# a = int(a)            # complex --> int    ====> ERROR (not possible)

# a = float(a)          # complex --> float  ====> ERROR (not possible)

# x = complex(a)        # int to complex 
# y = complex(y)        # float to complexx
# z = complex(z)        # string to complex

# a = str(a)            # complex to string
print(type(a))
# print(x , y , z)





