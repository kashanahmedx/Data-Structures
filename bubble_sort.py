"""
Bubble Sort
-----------
Repeatedly compares adjacent elements and swaps them if they are in the wrong
order. After each pass, the largest remaining element "bubbles" to the end.

Time Complexity:
    Best    : O(n)    (already sorted, thanks to the early-exit flag)
    Average : O(n^2)
    Worst   : O(n^2)
Space Complexity: O(1)
Stable  : Yes
In-place: Yes

Advantages:
    - Very simple to understand and implement
    - Stable and in-place
    - Detects an already sorted list (O(n) best case with the flag)

Disadvantages:
    - Very slow on large lists (O(n^2))
    - Many swaps, so it is rarely used in practice
"""


def bubble_sort(arr):
    arr = arr.copy()  # do not modify the original list
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # no swaps means the list is sorted
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted  :", bubble_sort(data))
