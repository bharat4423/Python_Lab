def dict_display_capitals(capitals):
  print(capitals)

def dict_add_elements(capitals):
    pass

def dict_remove_element(capitals):
    del capitals
    print(capitals)
        
def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print(" Please enter a list Comma seperated dictionary elements that you would want to perform opertion upon")
 
    capitals= {}
    for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        temp_list = dict_elem.split(":")
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()
        
    while (True):
        print("\n ***************Menu********************")
        print("Operations supported by our program are :")
        print(" 1: Display number of elements in the capitals collections ")
        print(" 2: Add an element to the capitals collections like --->Afganisthan : kabul")
        print(" 3: Add multiple elemennts to the capitals collections like --> albania :Tirana,Algeria:Algerias,andorraL:Andorraa la vella")
        print("4 : Remove an element from the collections ")
        print( "5 : exit the program")
        
        choice = int(input("Please enter the choice:"))
        if choice ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_elements (capitals)
        elif choice ==3:
            dict_add_elements (capitals)
        elif choice ==4:
            dict_add_elements (capitals)
        elif choice ==5:
            break
        else:
            print("Invalid input,Please Try Again !!!")
            
my_dict_store()            
               

  