# ─── Subroutines (functions) ───────────────────────────────────────────────────

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


# ─── Main program ──────────────────────────────────────────────────────────────

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

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        result = "Error: invalid choice"

    print(f"\nResult: {result}")


main()
