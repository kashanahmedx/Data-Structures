"""
Selection Sort
--------------
Repeatedly finds the minimum element from the unsorted part and places it at
the beginning of the unsorted part.

Time Complexity:
    Best    : O(n^2)
    Average : O(n^2)
    Worst   : O(n^2)
Space Complexity: O(1)
Stable  : No (in the standard swap-based version)
In-place: Yes

Advantages:
    - Simple to understand and implement
    - Makes at most n-1 swaps (good when writing/swapping is expensive)
    - In-place, needs no extra memory

Disadvantages:
    - Always O(n^2), even if the list is already sorted
    - Not stable
    - Slow on large lists
"""


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)
    print("Sorted  :", selection_sort(data))
