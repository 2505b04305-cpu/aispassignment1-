import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        s = input("Enter an integer (or 'q' to quit): ").strip()
        if s.lower() == 'q':
            break
        try:
            num = int(s)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")

if __name__ == "__main__":
    main()

import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        s = input("Enter an integer (or 'q' to quit): ").strip()
        if s.lower() == 'q':
            break
        try:
            num = int(s)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")

if __name__ == "__main__":
    main()