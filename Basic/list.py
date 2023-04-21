def my_list_store():
    print("\n Welcome to our list store !!! ")
    print("Please enter a list Comma sepearted that you would want to perform operation Upon")
    members = input(" Enter list name: ").split(",")
    
    def list_display_members(members):
        len(members)
        
    def list_add_element (members):
        members.append(input(" Enter new element "))
        len(members)
    def list_add_elements (members):
        members.extend(input(" Enter Multiple element ").split(','))
        len(members)
    def list_remove_element (members):
        members.pop(int(input(" Enter element for Remove")))
        len(members)
    def remove_last_element (members):
        members.pop()
        len(members)
    # def display_3_4_5_element (members):
        
        
    while(True):
        print(" \n *************** Menu Driven Program **************** ")
        print(" Operatinos suppported by our program are :")
        print(" 1: Display number of elements in the members list ")
        print(" 2: Add an element to the members collection like 'sehwag' ")
        print(" 3: Add elements to the members collection like ['David',' Bret', 'Sanju']")
        print(" 4: Remove the member from the collection at a given subscript ")
        print(" 5: Remove the last member from the collection ")
        print(" 6: Display third, fourth and fifth element from the collection ")
        print(" 7: Exit the Program ")
        choice = int(input(" Pelase Enter your choice : "))
        
        
        if choice == 1:
            list_display_members(members)
            print("Number of elements : ", members)
        elif choice == 2:
            list_add_element (members)
            print("Add an element : ", members)
        elif choice == 3:
            list_add_elements (members)
            print("Add Multiple an elements : ", members)
        elif choice == 4:
            list_remove_element (members)
            print("Remove elements : ", members)
        elif choice == 5:
            remove_last_element (members)
            print("Remove last elements : ", members)
        elif choice == 6:
            # display_3_4_5_element (members)
            print(members[2:5])
        elif choice == 7:
            break
        else :
            print( "Invalid Input , Please Try Again !!!! ")
            
my_list_store()