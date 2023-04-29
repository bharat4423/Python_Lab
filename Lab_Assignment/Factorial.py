# Q.1. Using for loop, write and run a Python program for this algorithm.
# Here is an algorithm to print out n! (n factorial) from 0! to 10! :
# 1. Set f = 1
# 2. Set n = 0
# 3. Repeat the following 10 times:
# a. Output n, "! = ", f
# b. Add 1 to n
# c. Multiply f by n

# f = 1
# for n in range(11):
#     print(n, "! = ", f)
#     n += 1
#     f *= n

# Q.2. Modify the program above using a while loop so it prints out all of the factorial values that are less than 2 billion. (You should be able to do this without looking at the output of the previous exercise.)



# n = int(input(" Enter your number : "))
n = 1
factorial = 1

while factorial < 2000000000:
    n += 1
    factorial *= n
    print(f"The factorial of {n} is {factorial}")


# input_num = int(input(" Enter your number : "))
# fact = 1
# cnt = input_num 
# while(cnt < 1 ):
#     fact *= cnt
#     cnt += 1
    
# if fact < 2000000 :
#     print(fact)
# else:
#     print(" Sorry Limit excedded of 2 Billion ")
    
    
    
# Q.1. Write a program that asks the user how many days are in a particular month, and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
# 1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30

