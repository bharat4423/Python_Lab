# Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console


raise_salary_percentage = int(input("Enter Percentage : " )) 
name= 'Gaurav'
print(name)
sal= float(input( "Enter Your salary "))
Incremented_salary = ((raise_salary_percentage/100) * sal )+sal

print(" Incremented salary " , Incremented_salary )
