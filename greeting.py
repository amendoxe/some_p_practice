# write a program that ask for a name and greets the user
def main():
    greet()
    name = input("What is your name? ")
    greet(name)


def greet(to="world"):
    "greets to the string to, or world by default"
    print("Hello,", to)


main()
