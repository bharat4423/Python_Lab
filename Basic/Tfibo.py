num1 = -1
num2 = 1
input_number = int(input("Enter numbers"))

while(True):
    sum = num1 + num2
    if sum > input_number:
        break
    print(sum,end= " ") 
    num1= num2
    num2= sum