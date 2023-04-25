import os

current_file_path = __file__
current_directory = os.getcwd()
target_folder_path = os.path.join(current_directory,'output')

if 'output' not in os.listdir(current_directory):
    os.mkdir(target_folder_path)
target_path = os.path.join(target_folder_path,'my_first_file_output.txt')
output_file = open(target_path,'w+')

for input_line in open('my_first_file.txt'):
    Hpcsa= input(" Enter text : \n")
    output_file.write(Hpcsa+input_line)

print("Your Data is added")
output_file.seek(0)  
print(output_file.read())