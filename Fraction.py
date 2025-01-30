class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, float) or isinstance(denominator, float):
            # This will check if it's a float, and makes it "0" if it is a float.
            self.numerator = 0
            self.denominator = 1
            return

        if isinstance(numerator, str) or isinstance(denominator, str):
            if not numerator.isnumeric() or not denominator.isnumeric():
                # This will check if the string is contains numeric characters.
                self.numerator = 0
                self.denominator = 1
                return

            numerator = int(numerator)
            denominator = int(denominator)

        if denominator == 0 or numerator == 0:
            raise ZeroDivisionError

        self.numerator = numerator
        self.denominator = denominator

        common_divisor = Fraction.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= common_divisor
        self.denominator //= common_divisor

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        if a > 0 or b > 0:
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.numerator == 0:
            return "0"
        return f"{self.numerator}/{self.denominator}"