# List in python


# creating list using []
List_1 = [1,2,3,4,5]

# printing List using print() function
print(List_1)


''' Accessing the elements or componenets 
of the list using index

eg. List[0] = 1 , List[1] = 2 , List[2] = 3 
    , List[3] = 4 , List[4] = 5 
'''
 # printing elements using index with function print()
print("All Elements of List accessed through index:", List_1[0] , List_1[1] , List_1[2] , List_1[3] , List_1[4])

# print(List[5]) # ==> No element at index = 5 so it shows error as 'list index out of range'


# 2) Change Item Value in List
# List can be modified like array using index
List_1[2] = 33 # modified 3rd element of the list (replaced 3 with 333)
print("\nAfter modification List is ",List_1)

# List_1[2] = 'shailesh' #--> Error show string imcompatable with int type 



''' List can contain different types of elements 
    eg. list = [integer , float , string , bool_value] --> Valid 
'''
a = [22 , 33.33 , 'shailesh' , True , False , "hello"]

print("\nCreated List with different data types: \n",a)


# a[1] = 'Why NO Erro?'   # No error as i am replacing float value with string value
# print("\nNew List(a) a[1]:\n",a)

print("\nChanging item from the specific positions:")
# 3) Replace (Changing) items with the specific range or replacing multiple values

a[1:3] = ['shailesh','shaileshMadne']  
# a[1] is changing from 'Why NO Error?' to 'shailesh'
# a[2] is changing from 'shailesh' to 'shaileshMadne'
print("changed from i = 1 and i = 2\n",a)
print()

# Replacing single index value with two different values

thislist = ['apple','banana','cherry','oragne','kiwi','mango']
print("Before replacing:\n",thislist)
print("Original Length of the thislist:\t",len(thislist))

''' 
1. If you insert more items than you replace, 
   the new items will be inserted where you specified, 
   and the remaining items will move accordingly:
2. The length also changes
'''
thislist[1:2] = ['balckcurrant','watermelon']
print("After Replacing a[1] with 'balckcurrant' and 'watermelon':\n",thislist,"\nLength after thislist[1:3] = \t",len(thislist))


thislist[1:5] = ['bucket']  # changed a[1] = a[2] = a[3] = a[4] = 'bucket'
print("After replacing the list:\n",thislist,"\nLength after thislist[1:5]:\t",len(thislist))





# List slicing = breaking the list into parts
# List[start_index : end_index]


# friends = ['vinit' , 'shreyas' , 'prathmesh' , 'saimanikanta' , 'ramkiran','girish','abhiram','akshay']

# print("Friends List:\n",friends)

# print(friends[0:4]) # op from 0th index to 3rd index i.e. it counts from 0 to (4-1)
# print(friends[0:8]) # all elements

# print(friends[:8])
# print(friends[0:]) # is same as print(friends[:8])


# Slicing with skipping values
# List[ Start_index : End_index : Skip_value]

# print(friends[0 : 8 : 2]) # -> skippin value between two

# To reverse list

# print("Reversing List:\n",friends[::-1])


''' Unpacking of the list
       --> Nothing but allocating separate variable for each value in the list
'''
# List = [1 , 33.3 , 'shailesh']
# x , y ,  z = List
# print("\nAfter Unpacking the list:")
# print("x =",x ,"\ty =", y ,"\tz =", z)





# if - else with List

if 'shailesh' in a:
    print("\nYes its present in the list")
else:
    print("\nNot present")