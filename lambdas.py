"""let's reproduce a bit of the exercise"""


def main():
    """still don't know how it is going to be so let's go to lambda"""
    expenses = {"amount": [5, 3, 2, 2], "category": "food"}
    total = amount_total(expenses)
    print(total)


def amount_total(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


main()
