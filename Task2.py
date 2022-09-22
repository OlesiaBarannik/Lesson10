def math():
    try:
        a = int(input("Please, enter two numbers A: "))
        b = int(input("Please, enter two numbers B: "))
    except ValueError:
        print("Could not convert data to an integer.")
        return False

    try:
        result = a ** 2 / b
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return False

    print(result)
    return result
math()




