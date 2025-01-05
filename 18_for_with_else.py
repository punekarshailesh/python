'''For loop with else
     Execution :
      -> 1st for loop starts 
                  -> after the condition fails then 
                                    -> it enters into else part

'''

print("Printing for loop with else statement:")
for i in range(1 , 10):
    print(i)
else:
    print("Printing is done")


print("\nPrinting while loop with else statement:")
i = 10
while i<=20:
    print(i)
    i = i+1
else:
    print("Done")