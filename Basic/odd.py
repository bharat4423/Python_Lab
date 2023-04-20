
# first = int(input("Enter First Number : "))
# last = int(input("Enter Last number : "))

# for num in range(first,last + 1):
#     if num % 2 != 0 :
#         print(num, end=" ")
        
        
def isOdd(num):
    if num % 2 != 0 :
          return num;
 
first = int(input("Enter First Number : "))
last = int(input("Enter Last number : "))

for num in range(first,last + 1):
    oddnum = isOdd(num)
    if oddnum is not None:
         print( oddnum,end=" " )


