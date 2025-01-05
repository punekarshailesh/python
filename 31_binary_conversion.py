'''
Decimal to binary conversion
eg. 10 ----------------> 1010
'''

# def power(n):
#     return n*n

num = int(input("Enter Number:\n"))

ans = 0
rem = 0
i = 0
val = 0.0
while num != 0:
    rem = num%10
    val = pow(10,i)
    ans = (ans * val) + rem
    i += 1
    num = num>>1

print(float(ans))