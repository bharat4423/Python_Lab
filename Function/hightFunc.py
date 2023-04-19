# print("Enter The Hight in Centimeter ")
# h_Cm = int(input("Height In Centimeter : " , ))

# h_inch = 0.394*h_Cm
# h_foot= 0.0328*h_Cm

# print("The Hight in Inches is ", round(h_inch,2))
# print (round(h_inch,2))

# print("The Height in feet is ")
# print(round(h_foot,2))

def hightFun(num) :
        return(round((num/30.48),2))
def inches(num1):
    return round((num/2.54), 2)
def feet_to_inches(feet):
    return round((feet * 12), 2)

num = int(input("Enter The Hight in Centimeter "))
print("The Hight in Foot is : ", hightFun(num))

num1 = int(input("Enter The Hight in Centimeter "))
print("The Hight in Inches is : ", inches(num1))

feet = int(input("Enter The Hight in Feet "))
print("The Foot in Inches is : ", feet_to_inches(feet))