class Fraction():
    """This python file implements an euclidean algorithm to find
    the gcd of two integers and also reduces a fraction into its
    simplest form.

    Authors : Lance De Guzman, Mishka Sy
    """
    def __init__(self, numerator=0, denominator=1):
        """Checks the fraction, its numerator, and its denominator

        Searches through the input to check if its a int, string, or float.
        It also checks if the input has a negative sign or trailing whitespaces.
        """
        if isinstance(numerator, float) or isinstance(denominator, float):
            self.numerator = 0
            self.denominator = 1
            return

        if isinstance(numerator, str):
            numerator = numerator.replace(" ", "")
            if '/' in numerator:
                parts = numerator.split('/')
                if len(parts) == 2:
                    numerator_part = parts[0]
                    denominator_part = parts[1]
                    if (numerator_part.lstrip('-').isdigit() and
                            denominator_part.lstrip('-').isdigit()):
                        numerator = int(numerator_part)
                        denominator = int(denominator_part)
                    else:
                        self.numerator = 0
                        self.denominator = 1
                        return
                else:
                    self.numerator = 0
                    self.denominator = 1
                    return

            elif numerator.lstrip('-').isdigit():
                numerator = int(numerator)
            else:
                self.numerator = 0
                self.denominator = 1
                return

        if isinstance(denominator, str):
            denominator = denominator.replace(" ", "")
            if not denominator.lstrip('-').isdigit():
                self.numerator = 0
                self.denominator = 1
                return

        if denominator == 0:
            raise ZeroDivisionError

        self.numerator = numerator
        self.denominator = denominator

        common_divisor = Fraction.gcd(
            abs(self.numerator), abs(self.denominator))

        if common_divisor != 0:
            self.numerator //= common_divisor
            self.denominator //= common_divisor

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def gcd(a, b):
        """Finds the gcd of two integers.

        Switches the two integers, a and b, then gets their gcd
        using the euclidean algorithm.
        """
        if a == 0 or b == 0:
            return 0
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    def get_numerator(self):
        """Returns the numerator as a string."""
        return str(self.numerator)

    def get_denominator(self):
        """Returns the denominator as a string."""
        return str(self.denominator)

    def get_fraction(self):
        """Returns the fraction as a string."""
        if self.numerator == 0:
            return "0"
        if self.denominator == 1:
            return str(self.numerator)

        return f"{self.numerator}/{self.denominator}"
