"""
Understanding the *args

- The *args is parameter, as other any. That is means that you can to call anything,
since that start with asterisk.

Example:

*xis

But by convention, we using *args for define it.

But what's *args ?

The parameter *args is used in function, put extras values informed as input in tuple.
Then since remember that tuple are unchanging

# Example


def sum(n1=1, n2=2, n3=3, n4=4):
    return n1 + n2 + n3 + n4


print(sum(4, 6, 9))

print(sum(4, 6)) #  TypeError
print(sum(4, 6, 7, 8)) #  TypeError

# Understanding the args


def add(name, email, *args):
    return sum(args)


print(add('jose','jose@gmail.com'))
print(add('jose','jose@gmail.com', 1))
print(add('jose','jose@gmail.com', 1, 2))
print(add('jose','jose@gmail.com', 1, 2, 3))


# Other Example use of *args

def verify_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Welcome Geek!'
    return 'i have not certain who you are '


print(verify_info())
print(verify_info(1, True, 'University', 'Geek'))
print(verify_info(1, 'University', 3.145))

"""


def add(*args):
    return sum(args)


print(add())
print(add(1, 2))

numbers = {1, 2, 3, 4, 5, 6}

# Unpacker

print(add(*numbers))

# OBS: The asterisk serve to that we inform Python that we are passing as argument a collection
# of data. Thus, He know that will need before to unpacker this data.

  