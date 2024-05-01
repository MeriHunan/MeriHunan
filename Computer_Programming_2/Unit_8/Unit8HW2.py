'''
Name:
Date:
Assignment:
See https://github.com/WLHS-Computer-Programming2/Unit-8/blob/main/Lesson-1/Period-8/main.py for instructions
'''

class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __eq__(self, other):
        return self.compare(other) == 0
    def times(self, other):
        return fraction(self.numerator * other.numerator, self.denominator * other.denominator) 
    def divide(self, other):
        return fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    def add(self, other):
        nnumerators = self.numerator * other.denominator
        nnumeratoro = self.denominator * other.numerator
        return fraction(nnumerators + nnumeratoro, self.denominator * self.numerator)
    def subtract(self, other):
        nnumerators = self.numerator * other.denominator
        nnumeratoro = self.denominator * other.numerator
        return fraction(nnumerators - nnumeratoro, self.denominator * self.numerator)
    def compare(self, other):
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