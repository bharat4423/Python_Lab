# try:
#     file1 = open('my_first_file.txt',"r")
#     print("I am reading the existing file -->\n", file1.read())
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     file1.write("Default creation was done in exception block")
#     # file1.writelines(['first_line\n','second_line\n','third_line'])
    
#     print("I am location ", file1.tell())
#     print("I am resetting it at 0 " , file1.seek(0))
#     print("I am location after resetting ", file1.tell())
#     print("I am reading just after writing-->", file1.read())
#     file1.close()

# program to read from one file and write to another file 
output_file= open('my_first_file_output.txt','w+')
for input_line in open('my_first_file.txt'):
    output_file.write('HPCSA '+input_line)

output_file.seek(0)    
print(output_file.read())