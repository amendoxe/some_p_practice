

def division(numerador, denominador):

    try:
        total = numerador / denominador
        return total
    except ZeroDivisionError:
        print("Division by Zero is Not defined")


print("type a number")
num1 = int(input())
print("type a number")
num2 = int(input())
print("the result is:", division(num1, num2))
