# n! = 1 * 2 * 3 * 4 * .... * (n-1) * n
# n! = [1 * 2 * 3 * 4 * ..... * (n-1)] * n
# n! = (n-1)! * n



# Uisng iterative approach
def factorial_iterative(num):
    fact = 1
    for i in range(num):
        fact = fact * (i+1)
    return fact



# Using recursive approach
def factorial_recursive(num):
    if(num == 0 or num == 1):
        return 1
    return factorial_recursive(num - 1) * num





num = int(input("Enter a number:\n"))

iterative_ans = factorial_iterative(num)
print("\nIterative Fuction:",iterative_ans)

recursive_ans = factorial_recursive(num)
print("\nRecursive Function:",recursive_ans)
