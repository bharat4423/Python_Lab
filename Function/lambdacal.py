# def hof(func,param1,param2= None):
#     return func(param1) if param2 is not None else func(param1,param2)

my_addition = lambda first_number, second_number: first_number + second_number
my_square = lambda first_number, second_number= None : first_number**2
my_exponenation = lambda first_number, second_number : first_number**second_number


# def my_cal():
#     print("#############>....MENU....<#############>")
#     print("1: Addtion ")
#     print("2: Square ")
#     print("3: Exponenation ")
    
#     choice = int(input("Please select your choice: "))
    
#     if choice == 1 :
#         first_num = int(input("Enter first Number : "))
#         second_num = int(input("Enter second Number : "))
#         returned_value = hof(my_addtionan,first_num,second_num)
#         print("The Addition of the number is :  ",returned_value)
        
#     elif choice == 2:
#         first_num = int(input("Please enter first Number : "))
#         returned_value = hof(my_square,first_num)
#         print("The Square of the number is : ",returned_value)
    
#     elif choice == 3:
#         first_num = int(input("Please enter First Number : "))
#         second_num = int(input("Please enter Second Number : "))
        
#         returned_value = hof(my_exponenation,first_num,second_num)
#         print("The Exponenation of the Number is : ",returned_value)
        
# def iterative_calculator():
#     while(True):
#         print("Lets Start  !!!!!")
#         my_cal()
#         choice = input("\n Do you want to continue (Y/N)").lower()
#         if choice == 'n' :
#             break
        
# iterative_calculator()

while(True):
    my_invocation_dict = {1: my_addition , 2 : my_square , 3: my_exponenation}
    print("Lets start   !!!! ")
    print("****************** MENU ************************")
    print("1: Addition ")
    print("2: Square ")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice : "))
    
    first_num = int(input("Please enter First number: "))
    if choice !=2 :
        second_num = int(input("Please enter Second number: "))
    
    print('Addition : ' if choice == 1 else 'Square : ' if choice == 2 else 'Exponentation: ' , end = ' ')
    print(my_invocation_dict.get(choice)(first_num,second_num))
       
    while(True):
            choice = input("Do you want to continue?").lower()
            if choice != 'n' and choice != 'y':                                
        
               print( "Invalid Input , Please Try Again !!!! ")
               
               continue
            else :
                break 
            if choice == 'n':
               break
