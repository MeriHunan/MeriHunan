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
    def set_number_served(self, new_number):
        self.number_served = new_number
    def increment_number_served(self):
        self.number_served += 1
class user():
    def __init__(self, first_name, last_name, describe_yours, gender, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.descr = describe_yours
        self.gender = gender
        self.birthday = birthday
        self.login_attempts = 0
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is a {self.gender} born on {self.birthday}. The user description is "{self.descr}"')
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
    def set_number_served(self, new_number):
        self.number_served = new_number
    def increment_number_served(self):
        self.number_served += 1
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attemps(self):
        self.login_attempts = 0


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
    print("Problem prints start here")
    # Problem 1
    restaurant_n = restaurant("Restaurant", "Mexican")
    print(restaurant_n.restaurant_name) # should print Restaurant
    print(restaurant_n.cuisine_type) # should print Mexican
    restaurant_n.describe_restaurant() # prints a description message
    restaurant_n.open_restaurant() # prints an open message
    # Problem 2
    meri_place = restaurant("Meri's place", "Armenian")
    armo_place = restaurant("Armo's place", "Mexican")
    cats_pasteries = restaurant("Cats and pasteries", "French")
    print(meri_place) # prints a description message
    print(armo_place) # prints a description message
    print(cats_pasteries) # prints a description message
    # Problem 3
    meri_hunanyan = user("Meri", "Hunanyan", "I like drawing and I am a very artistic person", "Female", "July 7th, 2009")
    armo_hunanyan = user("Armo", "Hunanyan", "I like Arduino", "Male", "September 28, 2014")
    albert_einstein = user("Albert", "Einstein", "I like playing the violin", "Male", "March 14, 1879")
    meri_hunanyan.describe_user() # prints a description message
    meri_hunanyan.greet_user() # prints hello "user name"
    armo_hunanyan.describe_user() # prints a description message
    armo_hunanyan.greet_user() # prints hello "user name"
    albert_einstein.describe_user() # prints a description message
    albert_einstein.greet_user() # prints hello "user name"
    # Problem 4
    print(restaurant_n.number_served) # should print 0
    restaurant_n.number_served = 12 # changes number_served to 12
    print(restaurant_n.number_served) # should print 12
    restaurant_n.set_number_served(5) # changes the number_served to 5
    print(restaurant_n.number_served) # should print 5
    restaurant_n.increment_number_served() # should increment the number served by 1
    print(restaurant_n.number_served) # should print 6
    # Problem 5
    print(meri_hunanyan.login_attempts) # should print 0
    meri_hunanyan.increment_login_attempts() # should increase by 1
    print(meri_hunanyan.login_attempts) # should print 1
    meri_hunanyan.reset_login_attemps() # should reset to 0
    print(meri_hunanyan.login_attempts) # should print 0
if __name__ == '__main__':
    main()