# num = int(input("Enter 1st number : "))
# num1 = int(input("Enter Last number : "))
# print("Your Prime Numbers")

# for n in range(num, num1 + 1):
#     if(n==1 or n==0):
#         for i in range(2, num):
#             if(n % i) == 0:
#                 break
#     else:
#         print(n)

def isPrime(n):
    if(n==1 or n==0):
        return False
    
    for i in range(2,n):
        if(n%i==0):
            return False
        return True
num = int(input("Enter 1st number : "))  
for i in range(1,num+1):
    if(isPrime(i)):
        print(i,end=" ")      