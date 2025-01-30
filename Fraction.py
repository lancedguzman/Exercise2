class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        pass

    def gcd(a, b):
        if a or b == 0:
            return 0
        elif a and b > 0:
            return abs(a % b)
        pass

    def get_numerator(self):
        self.get_numerator()
        pass

    def get_denominator(self):
        self.get_denominator()
        return str(self.get_denominator)
        pass

    def get_fraction(self):
        fraction = int(self.get_numerator()) / int(self.get_denominator())
        return fraction
        pass