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

# def isPrime(n):
#     if(n==1 or n==0):
#         return False
    
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#         return True
# num = int(input("Enter number : "))  
# for i in range(1,num+1):
#     if(isPrime(i)):
#         print(i,end=" ")      


# num = int(input("Enter number : ")) 
# # If given number is greater than 1
# if num > 1:
# 	# Iterate from 2 to n / 2
# 	for i in range(2, int(num/2)+1):
# 		# If num is divisible by any number between
# 		# 2 and n / 2, it is not prime
# 		if (num % i) == 0:
# 			print(num, "is not a prime number")
# 			break
# 	else:
# 		print(num, "is a prime number")
# else:
# 	print(num, "is not a prime number")

num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")