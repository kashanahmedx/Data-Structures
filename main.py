"""Runs all four sorting algorithms and compares their running time."""
import random
import time

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}


def main():
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Sample input:", sample)
    for name, func in ALGORITHMS.items():
        print(f"{name:15}: {func(sample)}")

    print("\nTiming on 2000 random numbers:")
    data = [random.randint(0, 10000) for _ in range(2000)]
    expected = sorted(data)
    for name, func in ALGORITHMS.items():
        start = time.perf_counter()
        result = func(data)
        elapsed = time.perf_counter() - start
        assert result == expected, f"{name} gave a wrong result!"
        print(f"{name:15}: {elapsed:.4f} seconds")


if __name__ == "__main__":
    main()
