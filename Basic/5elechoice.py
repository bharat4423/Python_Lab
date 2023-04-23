my_list = ["apple", "banana", "cherry", "Guava", "berry"]

try:
    index = int(input("Enter an index between 0 and 4: "))
    print(f"The value at index {index} is {my_list[index]}.")
except IndexError:
    print("Value not found.")
except ValueError:
    print("Invalid input. Please enter an integer between 0 and 4.")
