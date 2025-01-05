''' Practice set - chapter7
'''

# Q1 print multiplication table using for loop
num = int(input("Enter a number:\n"))

print("\nMultiplication table of",num,"using for loop:")
for i in range(1 , 11):
    print(num*i)


# Q2. Greeting to people
List1 = ['Harry','sachin','soham','rahul']
print()
for i in range(len(List1)):
    if List1[i].startswith('s'):
        print("Good Afternoon, "+ List1[i])
print()

# Q3 . printing multiplication table using while loop
print("\nMultiplication table of",num,"using while loop:")
i = 1
while i<=10:
    print(num * i)
    i = i+1


# Q4. checking whether the number is prime or not

print()
count = 0
for i in range(1 , num+1):
    if num%i == 0:
        count = count +1
    else:
        continue

if count == 2 :
    print(num,"is prime number")
else:
    print(num,"is not prime number")


# Q5. a) printing sum of first n natural number using for loop
'''
    Sum of n natural numbers
      sum = (n*(n+1))/2
'''

i = 1
sum = 0
while i<=num:
   sum += i
   i = i+1

print("\nSum of natural number is(While_Loop):",sum)

# Q5. b) printing sum of first n natural number using for loop
sum1 = 0
for i in range(1 , num+1):
    sum1 = sum1 + i

print("\nSum of natural number is(For_Loop):",sum1)


# Q6. a) Factorial of number i.e. 5! = 1*2*3*4*5  = 120
fact = 1
for i in range(1 , num+1):
    fact = fact * i

print("\nFactorial of",num,"is:\t",fact)

# Q6. b) Factorial of number using while_loop
fact = 1
i = 1
while i<=num:
    fact = fact * i
    i += 1

print("\nFactorial using While_Loop of",num,"is:\t",fact)


# Q8. pattern printing:
'''
*
**                  --> n = 3
***
'''
n = int(input("Enter number:\n"))
for i in range(1 , n+1):
    print("* "*(i))

for i in range(n,1):
    print(i)