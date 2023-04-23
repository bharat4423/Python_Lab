s1 = "Ault"
s2 = "Kelly"

def new_string(x,y):
    list=[i for i in x]
    list.insert(len(x)//2,y)
    print(''.join(list))
new_string(s1,s2)