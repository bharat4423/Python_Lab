num1 = -1
num2 = 1
input_number = int(input("Please enter the number till which you want to  print fibonacci sequence ?"))
while(True):
    sum = num1+num2
    if sum > input_number:
        break
    print(sum,end= " ") 
    num1 = num2
    num2 = sum
    