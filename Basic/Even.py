
# first = int(input("Enter First Number : "))
# last = int(input("Enter Last number : "))

# for num in range(first,last + 1):
#     if num % 2 == 0 :
#         print(num, end=" ")
        
        
def isEven(num):
    if num % 2 == 0 :
          return num;
 
first = int(input("Enter First Number : "))
last = int(input("Enter Last number : "))

for num in range(first,last + 1):
    Evennum = isEven(num)
    if Evennum is not None:
         print( Evennum,end=" " )


