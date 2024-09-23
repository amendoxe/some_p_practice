def main():
    numerador = get_input("numerador: ")
    denominador = get_input("denominador: ")
    division(numerador, denominador)


def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enteros por favor")


def division(n, d):
    try:
        print(n/d)
    except ZeroDivisionError:
        print("Division by zero is not defined")


main()
