print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Assignment: 
Date: 
"""
#Problem 1
class vehicle():
    # constructor
    def __init__(self, number_wheels: int, number_occupants: int, color = "black")->None:
        self.wheels = number_wheels
        self.occupants = number_occupants
        self.color = color
        self.max_occupancy = 5
    def add_n_occupants(self,n:int)-> int:
        """
        When this method is called the number of occupants is increased by n. If the number_occupants
        is higher then 5 then it will not perform the addition and will print an error message
        
        Intake:
        ---------
            n(int) - the number occupants are increased by

        Return:
        ---------
            int - the new number of occupants
        """
        if self.occupants + n > 5:
            print("Too many people! Can't be higher then 5.")
            raise ValueError
        else:
            self.occupants += n
        return self.occupants

def main() -> None:
    """
    
    The space to do all the tests in

    Intake:
    --------
    None

    Return:
    --------
    None
    """
    car1 = vehicle(2, 1, "red") # occupants
    car2 = vehicle(18, 3, "green") # color
    car3 = vehicle(11, 3)
    print(car3.color) # black
    print(car1.occupants) # 1
    print(car2.color) # green
    print(car1.add_n_occupants(3)) # 4
    try:
        print(car2.add_n_occupants(3)) # error message
    except ValueError:
        print(f"Currently you have {car1.occupants}")
              
if __name__ == '__main__':
    main()