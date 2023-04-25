class Employee():

    #class Variable
    department_name= " IT "
    
    def __init__(self, emp_id, emp_salary, mgr_id):
        
        # instance variableside
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.mgr_id = mgr_id
       
        # instance method
    def  display_emp_details(self) :
        print(f'emp_id : {self.emp_id} emp_salary : {self.emp_salary} mgr_id {self.mgr_id}')
    
       
# main method
def main():
    
    EMP=input("Enter emp id : ")
    Sal=input("Enter Emp Salary : ")
    MGR=input("Employee Maneger ID : ")
    
    first_employee = Employee(EMP,Sal,MGR)  
    print(type(first_employee))
    first_employee.display_emp_details()
      
main()