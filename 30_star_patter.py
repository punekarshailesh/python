'''
***
***              --->  for n = 3
***
'''
n = int(input("Enter number  of lines you want:\n"))
print("\nUsing For Loop:")
for i in range(n):
    print("*" * n)


print("\nUsing whileLoop:")
i = 0
while(i<n):
    print("*"*n)
    i += 1


'''
*
**         --->  for n = 3
***
'''
print("\nUsing For Loop:")

for i in range(n):
    print("*"*(i+1))

print("\nUsing while Loop:")
i = 0
while i<n:
    print("*"*(i+1))
    i+=1
    


'''
***
**                --> n = 3
*
'''
print("\nUsing For Loop:")

for i in range(n):
    print("*"*(n-i))

print("\nUsing while Loop:")
i = 0
while i<n :
    print("*"*(n-i))
    i += 1


'''
1 1 1
2 2 2    --> n = 3
3 3 3
'''
print("\nUsing for loop:")
for i in range(1 , n+1):
    for j in range(1 , n+1):
        print(i , end=" ")
    print()

print("\nUsing while loop:")
i = 0
# j = 0
while i<n:
    j = 0
    while j <n:
        print(i+1 , end=" ")
        j += 1
    print()
    i += 1


'''
1 2 3 4
1 2 3 4
1 2 3 4    ---> n = 4
1 2 3 4
'''
print("\nUsing for loop:")
for i in range(1 , n+1):
    for j in range(1 , n+1):
        print(j , end=" ")
    print()

print("\nUsing while loop:")
i = 0 
j = 0
while i<n:
    j = 0        
    while j<n:
        print(j+1 , end=" ")
        j += 1
    i += 1
    print()
'''
 for eg. n = 4 
as j comes out of loop its value is 4,
  so it always failse the while condition,
    which is j<n and in next iteration of i = 1
    in that j remains 4 and the 4<4 fails so it will not enter,
    while loop and prints new line only
i = 0 
j = 0
while i<n:
    # j = 0        if this j is intitialized outside loop
    while j<n:
        print(j+1 , end=" ")
        j += 1
    i += 1
    print()
    
    output:
 i = 0    1 2 3 4    (only when j is initialized outside or before  this while i<n: loop)
 i = 1
 i = 2
 i = 3

'''


'''
3 2 1
3 2 1                n = 3
3 2 1
'''
print("\nUsing for loop:")
for i in range(1 , n+1):
    for j in range(1 , n+1):
        print(n-j+1 , end=" ")
    print()

print("Using while loop:")
i = 0
j = 0
while i<n:
    j = 1
    while j<=n:
        print(n-j+1,end=" ")
        j += 1
    i += 1
    print()


'''
1 2 3
4 5 6     for n = 3
7 8 9
'''

print("\nUsing for loop:")
count = 1
for i in range(n):
    for j in range(n):
        print(count,end=" ")
        count += 1
    print()

print("Using while loop:")
i = 0
j = 0
count = 1
while i<n:
    j =0
    while j<n:
        print(count,end=" ")
        count = count + 1
        j += 1
    i += 1
    print()


# complement to the above solution
# store = 1
# for i in range(1 , n+1):
#     i = store
#     for j in range(n):
#         print(i,end=" ")
#         i += 1
#     store = i
#     print()


'''
1
2 3              for n = 3
4 5 6
'''

print("\nUsing for loop:")
for i in range(1 ,n+1):
    for j in range(0 ,i):
        print(i,end=" ")
    print()
print("Using while loop:")
i = 1
# j = 0
while i<=n:
    j = 0
    while j<i:
        print(i,end="")
        j += 1
    i += 1
    print()



'''
1
2 3              n = 4
4 5 6
7 8 9 10
'''
print("\nUsing for loop:")
count = 1
for i in range(1 ,n+1):
    for j in range(1, i+1):
        print(count,end=" ")
        count = count + 1
    print()
    
print("Using while looop:")
i = 1
count = 1
j = 0
while i<=n:
    j = 1
    while j<=i:
        print(count,end=" ")
        count += 1
        j += 1
    i += 1
    print()


'''
1
2 3       
3 4 5           n = 4
4 5 6 7
'''

print("\nUsing for loop:")
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
        i += 1
    print()

print("Using while loop:")
i = 1
j = 0
value = 0
while i in range(n+1):
    j = 1
    value = i
    while j<=i:
        print(value,end=" ")
        value += 1
        j += 1
        # break
    i += 1
    print()


'''
1
2 1                  n = 4
3 2 1
4 3 2 1
'''

print("\nUsing both while + for loop:")
j = 0
for i in range(1 , n+1):
    j = i
    while j>=1:
        print(j,end=" ")
        j = j - 1
    print()

print("Another method:")
value = 0
for i in range(1 , n+1):
    value = i
    for j in range(1 , i+1):
        print(value,end=" ")
        value -= 1
    print()

print("One more method using (i - j + 1):")
for i in range(1 , n+1):
    for j in range(1 , i+1):
        print(i-j+1 , end=" ")
    print()


