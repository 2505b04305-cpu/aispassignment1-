# ...existing code...

from typing import Iterable, Optional

def largest_number(values: Iterable[float]) -> float:
    """Return the largest number in values without using built-in max().
    Raises ValueError for empty input.
    """
    iterator = iter(values)
    try:
        largest = next(iterator)  # start with the first item
    except StopIteration:
        raise ValueError("largest_number() arg is an empty iterable")

    for v in iterator:
        # compare each value and update largest if current value is greater
        if v > largest:
            largest = v
    return largest


if __name__ == "__main__":
    sample = [1, 3, 5, 2, 4]
    print("List:", sample)
    print("Largest:", largest_number(sample))
# ...existing code...