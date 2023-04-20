n = int(input("Enter first Number "))

k = int(input("Enter Second Number "))

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()