def print_tringle(higher_limit):
    i=1
    while(i<=higher_limit):
        print('*' , end=' ')
        i = i+1
        
def print_reverse_tringle(higher_bound):
    for num in range(higher_bound,0,-1):
        print('*', end = ' ')
        
        
inp_rows = int(input("please enter number of rows "))//2
for row in range(1,inp_rows+2):
    print_tringle(row)
    print(' ')
    