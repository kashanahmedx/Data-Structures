"""
Insertion Sort
--------------
Builds the sorted list one element at a time by taking the next element and
inserting it into its correct position among the already sorted elements
(like sorting playing cards in your hand).

Time Complexity:
    Best    : O(n)    (already sorted)
    Average : O(n^2)
    Worst   : O(n^2)  (reverse sorted)
Space Complexity: O(1)
Stable  : Yes
In-place: Yes

Advantages:
    - Simple and easy to implement
    - Very fast on small or nearly sorted lists
    - Stable and in-place
    - Online: can sort data as it arrives

Disadvantages:
    - O(n^2) on large or random lists
    - Many shifts when the list is in reverse order
"""


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift larger element to the right
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original:", data)
    print("Sorted  :", insertion_sort(data))
