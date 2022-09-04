"""Classes for melon orders."""

from datetime import datetime
from random import randint

# datetime.now() is to get current time


class AbstractMelonOrder:

    order_type = "Abstract"
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        base_price = randint(5, 9)
        now_date = datetime.now()
        if now_date.date().isoweekday() >= 1 and now_date.date().isoweekday() <= 5:
            # strftime("%H)
            if int(now_date.strftime("%H")) >= 8 and int(now_date.strftime("%H")) <= 11:
                base_price = base_price + 4
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        super().__init__(species, qty)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed


class TooManyMelonsError(ValueError):
    pass
