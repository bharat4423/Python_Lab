# program to read from one file and write to the same file 
input_file = open('my_first_file.txt')
temp_data = input_file.readlines()
input_file.close()

output_file= open('my_first_file.txt','w+')
for input_line in temp_data:
    output_file.write(' HPCSA '+input_line)

output_file.seek(0)    
print(output_file.read())