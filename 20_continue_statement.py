'''continue statement:
'''


for i in range(4):
    print("Printing")
    if i == 2:
        continue
    print(i)



# even nos priting using continue statement
print("\nprinting even nos using conitnue_statement:")
for i in range(1 , 10):
    if i%2 != 0:
        continue
    print(i)


# odd nos - continue
print("\nPrinting odd nos using continue_statement:")
for i in range(1 , 10):
    if i%2 == 0:
        continue
    print(i)