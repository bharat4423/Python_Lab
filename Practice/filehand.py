# file1 = open('geek.txt','wt+')
# file2 = open('bharat.txt', 'rt')
# for each in file1:
#     print(each,end=' ')
    # file2.write(each)
    
# f = open("file1.txt","w")
# for each in f:
#     print(f.write(),end="")

# f = open("file2.txt","r")
# print(f.readline(),end="")

# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command \n")
file.write("It allows us to write in a particular file")
file.close()
