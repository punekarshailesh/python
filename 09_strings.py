   # strings


#    Representation of strings
str1 = 'Hi'
print(str1)
str2 = "shailesh,"
print(str2)
str3 = '''Good Morning''' # Triple quotes used when we have multiple lines present
print(str3)
print("Ans = ",str3[:-8])
print("Ans = ",str3[-8:] , " " , str3[:2:3])
print(str1,str2,str3)

# Concatanation of strings

# 1) combining 2 strings
str4 = str1 +" "+ str2
print(str4)

# 2) combining 3 strings
str5 = str1 + " " + str2 + ", " + str3
print(str5)


# Slicing of string
# indexing starts with the 0 till length-1

name = 'shailesh'

'''
     # positive indexing
                s  h  a  i  l  e  s  h
                0  1  2  3  4  5  6  7
     # negative indexing
               s   h   a   i   l   e   s   h
              -8  -7  -6  -5  -4  -3  -2  -1

                '''


print(name[0 : 8])
print(name[1 : 8])
print(name[:8]) # is same as name[0 : 8]
print(name[0 :]) # is same as name[0 : 8]
print(name[1:]) 
print(name[1:8])# is same as name[1 : 8]
print(name[-1]) # Here if we donot know the length of the string then we can directly use -1


# Slicing with skip value

string1 = input("Enter string:\n")
d = string1[0::2]
print(d)



x = 'Python '
y = 'is '
z = 'awesome'
print(x + y + z)


def fun():
   global x 
   x = 'awesome'
   print("shailes is "+ x)


   fun()