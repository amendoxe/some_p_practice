"""A greeting program I guess"""


def main():
    """Greeting program"""
    greet()
    print("What is your name?")
    name = input()
    greet(name)
    print("the other way")
    print()
    greet_format()
    greet_format(name)


def greet(to="World"):
    '''greets to the string to, world by default'''
    print("Hello, " + to)


def greet_format(to="Python world!"):
    '''Another way to greet, I guess'''
    print(f"Hello, {to}")


main()
