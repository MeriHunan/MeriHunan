print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Assignment: 
Date: 
"""

class restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def __str__(self):
        return f'The name of the {self.cuisine_type} restaurant is "{self.restaurant_name}"'
    def describe_restaurant(self):
        print(self)
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
class user():
    def __init__(self, first_name, last_name, describe_yours, gender, birthday,):
        self.first_name = first_name
        self.last_name = last_name
        self.descr = describe_yours
        self.gender = gender
        self.birthday = birthday
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is a {self.gender} born on {self.birthday}. The user description is "{self.descr}"')
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
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
    restaurant_n = restaurant("Restaurant", "Mexican")
    print(restaurant_n.restaurant_name)
    print(restaurant_n.cuisine_type)
    restaurant_n.describe_restaurant()
    restaurant_n.open_restaurant()
    # Problem 2
    meri_place = restaurant("Meri's place", "Armenian")
    armo_place = restaurant("Armo's place", "Mexican")
    cats_pasteries = restaurant("Cats and pasteries", "French")
    print(meri_place)
    print(armo_place)
    print(cats_pasteries)
    # Problem 3
    meri_hunanyan = user("Meri", "Hunanyan", "I like drawing and I am a very artistic person", "Female", "July 7th, 2009")
    armo_hunanyan = user("Armo", "Hunanyan", "I like Arduino", "Male", "September 28, 2014")
    albert_einstein = user("Albert", "Einstein", "I like playing the violin", "Male", "March 14, 1879")
    meri_hunanyan.describe_user()
    meri_hunanyan.greet_user()
    armo_hunanyan.describe_user()
    armo_hunanyan.greet_user()
    albert_einstein.describe_user()
    albert_einstein.greet_user()
    # Problem 4
    print(restaurant_n.number_served)
    restaurant_n.number_served = 12
    print(restaurant_n.number_served)
if __name__ == '__main__':
    main()