#  tag=charlesknell - Menu module

#  This module
#  should define a function, also called menu. The function takes any number of key
#  value pairs as arguments. Each value should be a callable, a fancy name for a function
#  or class in Python.
#  When the function is invoked, the user is asked to enter some input. If the user
#  enters a string that matches one of the keyword arguments, the function associated
#  with that keyword will be invoked, and its return value will be returned to menu’s caller.
#  If the user enters a string that’s not one of the keyword arguments, they’ll be given an
#  error message and asked to try again.

def menu(**kwargs):
    while True:
        option_string = " or ".join(kwargs.keys())
        choice = input(f'Enter an option: {option_string} : ')
        if choice in kwargs.keys():
            return kwargs[choice]()

        print("Error: Not a valid option")


if __name__ == '__main__':
    def func1():
        return "1"


    def func2():
        return "2"


    def func3():
        return "3"


    result = menu(a=func1, b=func2, c=func3)
    print("Result", result)
