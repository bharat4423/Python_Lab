

# print(" Welcome Our Number Pattern System")
# row = int(input(" Enter pattern : "))

# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1 ):
#         print(j, end=" ")
        
#     print(" ")


n = int(input(" Enter pattern : "))

# Outer loop for the number of rows
for i in range(1, n+1):
    # Inner loop for the spaces
    for j in range(1, n-i+1):
        print(" ", end=" ")
    # Inner loop for the decreasing numbers
    for k in range(i, 0, -1):
        print(k, end=" ")
    # Inner loop for the increasing numbers
    for l in range(2, i+1):
        print(l, end=" ")
    # Print a newline character after each row
    print()
