print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Assignment: 
Date: 
"""
#Problem 1
class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
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
    # Problem 1
    restaurant = restaurant("restaurant", "Mexican")
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)

if __name__ == '__main__':
    main()