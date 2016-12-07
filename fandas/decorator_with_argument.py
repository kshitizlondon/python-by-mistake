from functools import wraps


def currency(sign):
    """
    :param string sign:
    :return function currency_wrapper:
    """
    def currency_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            """
            :return string:
            """
            return sign + str(f(*args, **kwargs))

        return wrapper

    return currency_wrapper


class Product:
    """
    Simple class made for product to manage simple attributes likes name and price.
    """

    def __init__(self, name, price):
        """
        :param string name:
        :param float price:
        """
        self.name = name
        self.price = price

    @currency('£')
    def price_with_tax(self, tax_rate_percentage):
        """
        :param float tax_rate_percentage:
        :return string: Becuase currency decorator is used.
        """
        return self.price * (1 + (tax_rate_percentage * .01))


if __name__ == '__main__':
    apple = Product('apple', 5.4)
    print(apple.price_with_tax(5))

