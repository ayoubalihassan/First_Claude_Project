def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("-----------------")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("  1 - Add")
    print("  2 - Subtract")
    print("  3 - Multiply")
    print("  4 - Divide")

    choice = input("\nYour choice (1/2/3/4): ")

    try:
        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            print("Error: invalid choice")
            return
        print(f"\nResult: {result}")
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
