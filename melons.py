from random import randint
"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """A parent class for all melon orders"""
    shipped = False

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species.lower()
        if qty > 100:
            raise TooManyMelonsError
        else:
            self.qty = qty

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def get_base_price(self):
        """Get a random base price for splurge pricing."""
        return randint(5, 9)


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty <= 10:
            return total + 3
        else:
            return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Mark inspection true or false.

        Takes a Boolean value, passed, and sets self.passed_inspection to it.
        """

        self.passed_inspection = passed


class TooManyMelonsError(ValueError):
    """Exception that occurs when there are more than 100 melons."""

    def __init__(self):
        super(TooManyMelonsError, self).__init__("No more than 100 melons!")
