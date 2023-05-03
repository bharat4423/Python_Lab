def fab():
    num = int(input(" Enter the number : "))
    
    sum = 0
    a = 0 
    b = 1
    
    for i in range(num):
        sum = a+b
        a=b
        b=sum
        
        print(sum)
        
fab()