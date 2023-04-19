# Get the height from the user in cms and display the user height back to console
# in foot/feet and inches


print("Enter The Hight in Centimeter ")

h_Cm = int(input("Height In Centimeter : " , ))

h_inch = 0.394*h_Cm
h_foot= 0.0328*h_Cm

print("The Hight in Inches is ")
print (round(h_inch,2))

print("The Height in feet is ")
print(round(h_foot,2))

