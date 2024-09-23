"""What is the number with error handling maybe"""


def main():
    '''call for the input function'''
    prompt = "What is x? "
    get_input(prompt)


def get_input(prompt):
    """we are getting the input"""
    # error handling when receiving a string
    # keep askig for the value if theres the ValueError
    while True:
        try:
            x = int(input(prompt))
            print(f"x is: {x}")

        except ValueError:
            pass


main()
