# ...existing code...
def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]

def main():
    while True:
        s = input("Enter a string (or press Enter to quit): ")
        if s == "":
            break
        print("Reversed:", reverse_string(s))

if __name__ == "__main__":
    main()
# ...existing code...