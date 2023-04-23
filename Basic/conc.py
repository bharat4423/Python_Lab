# Hardcore #
# list1 = ["M", "na", "i", "Bha"] 
# list2 = ["y", "me", "s", "rat"]
# list3 = [list1 + list2 for list1, list2 in zip(list1, list2)]
# print(list3)

# User input
list1 = input("Enter the list 1 : ").split(',')
list2 = input("Enter the list 2 : ").split(',')
list3 = [list1 + list2 for list1, list2 in zip(list1, list2)]
print(list3)

