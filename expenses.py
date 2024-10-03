"""build a expense tracker with functions like
    1 Adding expense
    2 List all expenses
    3 Show total expense
    4 filter by expense by category
    5 exit
    """


def main():
    """Show menu and take input"""
    expenses = []
    while True:
        print(
            "\nWhat do you want to do?\n 1. Add expense"
            "\n 2. Show all expenses\n 3. Show total"
            "\n 4. Filter by expense \n 5. Exit"
        )
        choice = input()
        if choice == "5":
            break
        elif choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_all_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            filter_by_expense(expenses)
        else:
            pass


def add_expense(expenses):
    """Create a new expense item in expenses with amount, and category"""
    while True:
        try:
            print("Enter the amount:")
            amount = int(input())
            break
        except ValueError:
            pass
    print("What is the category?:")
    category = input()
    expenses.append({"amount": amount, "category": category})


def list_all_expenses(expenses):
    """Print all the expenses with amount and category"""
    for expense in expenses:
        print(f"amount: {expense["amount"]}, category: {
              expense["category"]}")


def show_total(expenses):
    """print the sum of all expenses amount"""
    # now we are going to try some lambda functions
    print("total:", sum(map(lambda expense: expense["amount"], expenses)))


def filter_by_expense(expenses):
    '''make a list of the filtered items in expenses'''
    category = input("which category do you want to check? ")

    filtered_expenses = filter(
        lambda expense: expense["category"] == category, expenses)

    list_all_expenses(filtered_expenses)


main()
