'''
Name: Meri Hunanyan
Date: 4/30/204
Assignment: Unit 8 HW 2 
See https://github.com/WLHS-Computer-Programming2/Unit-8/blob/main/Lesson-1/Period-8/main.py for instructions
'''

class fraction:
    def __init__(self, numerator, denominator):
        """
        Constructor def

        Parameters:
        ------------
        numerator(int) - The numerator of the fraction being created
        denominator(int) - The denominator of the fraction being created

        Return:
        ---------
        None
        """
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        """
        Enables us to print the fraction

        Parameters:
        ------------
        None

        Return:
        --------
        str - what will print when printed
        """
        return f"{self.numerator}/{self.denominator}"
    def __eq__(self, other: "fraction"):
        """
        Compares itself to the other fraction and returns true if equal and no if not
        
        Parameters:
        ------------
        other(fraction) - the function we are comparing ourselves to
        
        Return:
        bool - True if equal, false if not
        """
        return self.compare(other) == 0
    def times(self, other: "fraction") -> "fraction":
        """
        Multiplies the class instance with the given, other fraction class instance

        Parameters:
        ------------
        other(fraction) - The fraction we are multiplying with
        
        Return:
        ---------
        fraction - The answer. Not simplified 
        """
        return fraction(self.numerator * other.numerator, self.denominator * other.denominator) 
    def divide(self, other: "fraction") -> "fraction":
        """
        Divides the class instance with the given, other fraction class instance
        
        Parameters:
        ---------------
        other(fraction) - The fraction we are dividing to
        
        Return:
        --------
        fraction - The answer. Not simplified 
        """
        return fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    def add(self, other: "fraction") -> "fraction":
        """
        Adds the class instance with the given instance
        
        Parameters:
        -------------
        other(fraction) - The fraction that is added

        Return:
        ----------
        fraction - The answer. Not simplified
        """
        nnumerators = self.numerator * other.denominator
        nnumeratoro = self.denominator * other.numerator
        return fraction(nnumerators + nnumeratoro, self.denominator * self.numerator)
    def subtract(self, other: "fraction") -> "fraction":
        """
        Subtarcts the given, other class instance from this class instance.
        
        Parameters:
        --------------
        other(fraction) - the fraction we are subtracting with

        Return:
        ----------
        fraction - The answer. Not simplified
        """
        nnumerators = self.numerator * other.denominator
        nnumeratoro = self.denominator * other.numerator
        return fraction(nnumerators - nnumeratoro, self.denominator * self.numerator)
    def compare(self, other: "fraction"):
        """
        Compares two fractions. Return 0 for equals, -1 for self is smaller then and 1 for self bigger then.

        Parameters:
        ------------
        other(fraction) - The fraction we are comparing our fraction to
        
        Return:
        ----------
        int - 0 for equal, -1 for self smaller then and 1 for self bigger then
        """
        nnumerators = self.numerator * other.denominator
        nnumeratoro = self.denominator * other.numerator
        if nnumerators > nnumeratoro:
            return 1
        elif nnumeratoro > nnumerators:
            return -1
        return 0
    
def main():
    """
    
    The space to do all the tests in

    Intake:
    --------
    None

    Return:
    --------
    None
    """
    f1 = fraction(1, 2)
    f2 = fraction(3, 4)
    f3 = fraction(4, 6)
    print("divide")
    print(f1.divide(f2)) # divide f1 with f3
    print(f1.divide(f3)) # divide f1 with f3
    print("add")
    print(f1.add(f3)) # add f1 with f3
    print("compare")
    print(f1.compare(f3))


# don't modify anyting below this
if __name__ == '__main__':
    main()