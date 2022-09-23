def math():
    try:
        a = int(input("Please, enter two numbers A: "))
        b = int(input("Please, enter two numbers B: "))
        result = a ** 2 / b
        print(result)
        
    except ValueError:
        print("Could not convert data to an integer.")
    except ZeroDivisionError:
        print("You cannot divide by zero")


math()

