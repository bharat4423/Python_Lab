# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Person)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 



class Person():
    #class Variables
    def __init__(self, in_name, place_of_residence):
        #Instance veriable
        self.name = in_name
        self.place = place_of_residence
        
        #Instance Method        
    def display_attributes(self):
        print(f'Name : {self.name} \n Place : {self.place}')
        
    #Static Method
    @staticmethod
    def display_details():
        print( 'This Person is relatives with Sister and Uncle')
            
        
   
class Sister(Person):
    def __init__(self, in_name, place_of_residence,exam_subjects):
        super().__init__(in_name, place_of_residence)
        self.exam_subject = exam_subjects
        
    def display_attributes(self):
        super().display_attributes()
        print(f'Exam Subjects : {self.exam_subject}')
    
    
class Uncle(Person):
    def __init__(self, in_name, place_of_residence,in_business):
        super().__init__(in_name, place_of_residence)
        self.business = in_business
        
    def display_attribute(self):
        super().display_attributes()
        print(f'Business : {self.business}')
        
        
def main():
           
    name = input(" Enter Name : ")
    place = input("Enter Place Name : ")
    exam_sub = input(" Enter Exam Subjects : ")
    busi_ness = input(" Enter Your Business Name : ")
    
    sis = Sister(name,place,exam_sub)
    unc = Uncle(name,place,busi_ness)
      
    sis.display_attributes()
    unc.display_attribute()
    print(Sister)
    print(Uncle)
    
main()
