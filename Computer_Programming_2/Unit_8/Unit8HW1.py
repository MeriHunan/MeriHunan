print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Assignment: 
Date: 
"""
#Problem 1
class vehicle():
    def __init__(self, number_wheels, number_occupants, color = "black"):
        self.wheels = number_wheels
        self.occupants = number_occupants
        self.color = color
        self.max_occupancy = 5
    def add_n_occupants(self,n:int)-> int:
        if self.occ + n > 5:
            print("Too many people")
            raise ValueError
        else:
            self.occ += n
        return self.occ

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
    print(car1.occupants())
    print(car2.color())
    print(car1.add_n_occupants(3))

if __name__ == '__main__':
    main()