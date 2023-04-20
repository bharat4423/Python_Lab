  
    
# num = int(input("Enter the number"))
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()
    
    

def fibonacci(num, i, j):
    num = i + j
    i = j
    j = num
          
num = int(input("Enter the number : "))
i, j = -1, 1
print("Fibonacci Series:", i, j, end=" ")
for i in range(2, num):
    fib = fibonacci(num, i,j )
print(fib, end=" ")
    
    