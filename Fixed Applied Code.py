def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def is_even(number):
    return number % 2 == 0

def buggy_loop():
    i = 0
    while i < 5:
        print("Loop iteration:", i)
        i += 1

def main():
    print("Adding numbers:", add_numbers(5, 3))
    print("Dividing numbers:", divide_numbers(10, 0))
    print("Is 4 even?", is_even(4))
    buggy_loop()

if __name__ == "__main__":
    main()

