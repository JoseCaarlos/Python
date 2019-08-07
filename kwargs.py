"""
**kwargs

We can to call those parameter of **xix, but by convention we to call of **kwargs

Those is only more one parameter, but different of *args that put extras values in tuple,
the **kwargs require that we use parameters named, and transform those parameter extras
in a dictionary


# Example

def colors_favorites( **kwargs):
    for person, color in kwargs.items():
        print(f"The color favorite of {person.title()} is {color}")


colors_favorites(marcos='green', julia='yellow', fernanda='blue', vanessa='white')


# OBS: The parameter *args and **kwargs aren't obligatory.

colors_favorites()

colors_favorites(geek='Navy')

# Example more complex


def greet_special(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'You received a greet Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'I am not sure who you are '


print(greet_special(geek='Python'))
print(greet_special(geek='Hello'))
print(greet_special())

# The our functions, we can have (IN THIS ORDER):
- parameter obligatory;
- *args
- Parameter default (not obligatory)
- **kwargs

def my_function(name, age, *args, unmarried=False, **kwargs):
    print(f"{name} have {age} years")
    print(args)
    print(unmarried)
    print(kwargs)
    print("\n\n")

my_function('jose', 20)
my_function('jose', 20, 4, 5, 6, unmarried=True)
my_function('Felipe', 34, you=True, i='not')
my_function('Carla', 19, java=False, python=True)

# Understand because is important keep order of parameters at declaration


# Function with a order correct parameters
# def show_info(a, b, *args, instructor='Geek', **kwargs):
#    return [a, b, args, instructor, kwargs]

# Function with the order incorrect of parameters
def show_info(a, b, instructor='Geek',*args, **kwargs):
    return [a, b, args, instructor, kwargs]

a = 1
b = 2
args = (3,)
instructor = 'Geek'
kwargs = {'lastname': 'University', 'jobRole': 'Instructor'}

print(show_info(1, 2, 3, lastname='University', jobRole='Instructor'))


# Unpack with **kwargs


def show_names(**kwargs):
    return f"{kwargs['name']} {kwargs['lastName']}"


names = {'name': 'Felicity', 'lastName': 'Jones'}

print(show_names(**names))

"""


def sum_multiple_number(a, b, c, **kwargs):
    print(a + b + c)

list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
sum_multiple_number(*list)
sum_multiple_number(*tuple)
sum_multiple_number(*set)

dict = dict(a=1, b=2, c=3)
sum_multiple_number(**dict)


# OBS: The key names in a dictionary must be same of parameters function

# dict = dict(d=1, e=2, f=3)
# sum_multiple_number(**dict)


sum_multiple_number(**dict, lang='Python')





