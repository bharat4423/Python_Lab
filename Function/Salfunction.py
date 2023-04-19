# Create function for Salary

def salary(ex_sal,raise_sal_per):
    return ((raise_sal_per/100) * ex_sal )+ex_sal

raise_sal_per = float(input("Enter Percentage : " ))
ex_sal= float(input( "Enter Your salary "))

Incremented_salary = salary(ex_sal,raise_sal_per)
print(" Incremented salary " , Incremented_salary )

