def Fizz_Buzz():
    num = int(input("Enter a Number: "))
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("Invalid Input")
    
while True:
    print("****************** MENU ************************")
    print("1: Fizz Buzz")
    print("2: Exit")
    choice = int(input("Enter a Choice: "))
    if choice == 1:
        Fizz_Buzz()
    elif choice == 2:
        break
    else:
        print("Invalid Choice")
        