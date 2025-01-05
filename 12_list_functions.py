'''List function 
  1 . Using string functions 
       a. list.replace() 
       b. list.find()
       c. list.endswith()
       d. list.startswith()
       e. list.append()
       f. list.insert()
       g. list.
       h
       '''

a = [22, 33.33, 'shailesh', True, False, "hello"]

# Modification in a
''' 1 . list.replace() 
        -> replaces the value
        -> only works on string
'''

# a = a[2].replace("shailesh" , "prathmesh") # --> this will create string with value prathmesh in a
# print(a)  # print only prathmesh

print("Before modification a is :\n", a)

# a[2] = a[2].replace('shailesh' , 'prathmesh')
# a[1] = a[1].replace(22 , 3223)       #    Error -> 'float' object has no attribute 'replace'
# a[3] = a[3].replace(True , 'MADNE' ) #    Error ->  Bool value cannot be replaced ('bool' object has no attribute 'replace')
# a[4] = a[4].replace(False , True)    #      -->same error as above statement

print("After modification a is :\n", a)


# 2. len() --> Gives the length of the list or number of elements in list
print("Length of list:\n", len(a))


# 3. list.endswith() - returns boolean value i.e. True or False only works on strings inside list

# gives same output as a[5].endswith("hello") i.e. => True
# print(a[5].endswith("o"))
# print(a[0].endswith(2))         # -> 'int' object has no attribute 'endswith'
# print(a[1].endswith(33.33))       # -> 'float' object has no attribute 'endswith'


''' 4. list.startswith()  
        -> returns Boolean value i.e. True or False
        -> only works on string literals
'''

# print(a[1].startswith(33.33)) # ->  'float' object has no attribute 'startswith'
# print(a[0].startswith(22))    # ->   'int' object has no attribute 'startswith'
# print(a[2].startswith("s"))  # -> True


''' 5. list.find()
        -> returns the index 
             (first occurence)
                 i.e. if it founds at 2 position then it will return index of the 1st position
        -> only works on strings
'''
# result = a[0].find(22)  # -> shows error 'int' object has no attribute 'find'
# -> as 'h' is present in 'shailesh' at index = 1 so it returns 1
# result = a[2].find('h')
# print(result)

'''
    4). Insert Items in the list
       -> Insert at given index without replacing existing values   
                list.insert(index , Value)
'''
print("\nInsert Function:\n")
a.insert(2,'HelloWorld')
print(a)
print("length:\t",len(a))

