def my_addition():
    first_num = int(input("Please enter First number:"))
    second_num = int(input("Please enter Second number:"))
    return  first_num+second_num

def my_square():
    first_num = int(input("Please enter First number:"))
    
    return first_num**2

def my_exponentation():
    first_num = int(input("Please enter First number:"))
    second_num = int(input("Please enter Second number:"))    
    return first_num**second_num


while(True):
        print(" \n *************** Menu Driven Program **************** ")
        print(" Operatinos suppported by our program are :")
        print(" 1: Addition ")
        print(" 2: Square ")
        print(" 3: Exponentation ")
        print(" 4: Exit the Program ")
               
        choice = int(input(" Pelase Enter your choice : "))
         
        
        if choice == 1:
  
            print("The Addition of the numbers is ", str(my_addition()))
        elif choice == 2:
            
            print("First number squared is  ", str(my_square()))
        elif choice == 3:
            
            print("First number raised to number second number is  ", str(my_exponentation()))
        elif choice == 4:
            break
        else :
            print( "Invalid Input , Please Try Again !!!! ")




