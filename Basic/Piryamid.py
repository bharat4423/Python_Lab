
total_rows = int(input("rows : "))     
for i in range(1,total_rows+1):
    for space in range(0,total_rows-i):
        print(" ", end = '')
    for star in range(0,2*i-1):
        print( "*",end = '')    
    print('')