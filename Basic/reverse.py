# list = [10, 20, 30, 40, 50]
# numbers = reversed(list)
# for i in numbers:
#     print(i)
    
    
user_input = input("Enter a list of numbers separated by spaces: ")
list = [int(num) for num in user_input.split()]

numbers = reversed(list)
for i in numbers:
    print(i)
