"""
Documented functions with DocString

OBS: We can have access the documentation of a function in Python
using the special property __doc__

We can still do Access to documentation with the function help()
"""

# Example


def say_hi():
    """ A function simple that return the string 'Oi' """
    return 'Oi'


def exponential(number, potential=2):
    """
    Function that return by default, squared number or number potency informed
    :param number: Number that we wish generate the exponential.
    :param potential: Potency that we want generate the exponential. by default is 2.
    :return: Return exponential of 'number' by 'potency'.
    """
    return number ** potential


print(exponential(4))

print(help(exponential))

print(exponential.__doc__)