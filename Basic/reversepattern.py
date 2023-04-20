# n = int(input("Enter first Number "))

# k = int(input("Enter Second Number "))

# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


def print_reverse_num(higher_bound):
    for num in range(higher_bound,0,-1):
        print(num, end= ' ')
        
input_row = int(input("rows: "))
for row in range(input_row,0,-1):
    print_reverse_num(row)
    print(' ')
    