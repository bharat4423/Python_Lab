# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 

class Tickets():
    #class Variables
    airline_name = "Kingfisher_Beer"
    
    #class method 
    def change_airline_name(air, air_country_name):
        air.airline_name = air_country_name
        
    def __init__(self, in_aircompany_name,in_departure,in_arrival_time,in_flightname,in_sitrow,in_sitnumber):
        #instance variables
        self.Aircompany_Name = in_aircompany_name
        self.Departure_Time = in_departure
        self.Arrival_Time = in_arrival_time
        self.Flight_Name = in_flightname
        self.SitRow_Name = in_sitrow
        self.SitNumber = in_sitnumber
        
    def display_Air_details(self):
        print(f'AirLine Name: - {self.Aircompany_Name } \n Air Departure Time {self.Departure_Time} \n Air Arriaval Time {self.Arrival_Time} \n Flight Name {self.Flight_Name} \n Sit Row {self.SitRow_Name} \n Sit Number {self.SitNumber}')
        
    @staticmethod
    def display_facilities():
        print('We are Providing Air Services Just Like Vijay Mallya AirLines')
        
def main():
       
    CompName = input(" Enter Air Company Name : ")
    ArrTime = float(input("Enter Arravial Time : ")) 
    DepTime = float(input(" Enter Departure Time : "))
    FltName = input(" Enter Flight Name : ")
    SitRnm = input(" Enter Sit Row Name : ")
    Sitnum = int(input(" Enter Sit Number : "))
    
    Plain = Tickets(CompName,DepTime,ArrTime,FltName,SitRnm,Sitnum)
    print(type(Plain))
    Plain.display_facilities()
    Plain.display_Air_details()
            
main()