class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, float) or isinstance(denominator, float):
            self.numerator = 0
            self.denominator = 1
            return

        if isinstance(numerator, str):
            numerator = numerator.replace(" ","")
            if '/' in numerator:
                parts = numerator.split('/')
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    numerator = int(parts[0])
                    denominator = int(parts[1])
                else:
                    self.numerator = 0
                    self.denominator = 1
                    return

            elif not numerator.isdigit():
                self.numerator = 0
                self.denominator = 1
                return
            else:
                numerator = int(numerator)

        if isinstance(denominator, str):
            denominator = numerator.replace(" ","")
            if not denominator.isdigit():
                self.numerator = 0
                self.denominator = 1
                return
            else:
                denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError

        self.numerator = numerator
        self.denominator = denominator

        common_divisor = Fraction.gcd(abs(self.numerator), abs(self.denominator))
        if common_divisor != 0:
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
        elif self.denominator == 0:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"