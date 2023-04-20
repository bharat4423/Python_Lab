def my_addition(first_num , second_num):
    return  first_num+ second_num

def my_square(first_num):
    return first_num**2

def my_exponentation(first_num , second_num):
    return first_num**second_num


first_num = int(input("Please enter First number:"))
second_num = int(input("Please enter Second number:"))

print("The Addition of the numbers is ", str(my_addition(first_num,second_num)))
print("First number squared is  ", str(my_square(first_num)))
print("First number raised to number second number is  ", str(my_exponentation(first_num , second_num)))
