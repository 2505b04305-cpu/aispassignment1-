# ...existing code...

def factorial_iterative(n: int) -> int:
    """Compute n! using an iterative loop.
    Raises ValueError for negative input.
    """
    if n < 0:
        
        # Factorial is not defined for negative integers
        raise ValueError("factorial() not defined for negative numbers")

    result = 1
    # Multiply result by each integer from 2 up to n
    for i in range(2, n + 1):
        result *= i  # accumulate the product
    return result


def factorial_recursive(n: int) -> int:
    """Compute n! using recursion.
    Raises ValueError for negative input.
    """
    if n < 0:
        # Factorial is not defined for negative integers
        raise ValueError("factorial() not defined for negative numbers")

    # Base case: 0! and 1! are 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


def main():
    # Get user input
    s = input("Enter a non-negative integer (or press Enter to quit): ").strip()
    if s == "":
        return

    try:
        n = int(s)
    except ValueError:
        print("Please enter a valid integer.")
        return

    try:
        print("Iterative result:", factorial_iterative(n))
        print("Recursive result:", factorial_recursive(n))
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
# ...existing code...