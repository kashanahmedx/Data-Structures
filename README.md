# Sorting Algorithms in Python

Implementations of four classic sorting algorithms with explanations of their
advantages, disadvantages, and time complexity.

## Files

| File | Description |
|------|-------------|
| `bubble_sort.py` | Bubble Sort |
| `selection_sort.py` | Selection Sort |
| `insertion_sort.py` | Insertion Sort |
| `merge_sort.py` | Merge Sort |
| `main.py` | Runs all algorithms and compares their speed |

## How to Run

```bash
python main.py            # compare all algorithms
python bubble_sort.py     # run a single algorithm
```

## Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |

## Advantages and Disadvantages

### Bubble Sort
**Advantages:** very simple; stable; in-place; detects sorted input (O(n) best case).
**Disadvantages:** very slow on large lists (O(n²)); many swaps.

### Selection Sort
**Advantages:** simple; at most n-1 swaps; in-place.
**Disadvantages:** always O(n²), even on sorted input; not stable.

### Insertion Sort
**Advantages:** fast on small or nearly sorted data; stable; in-place; works online.
**Disadvantages:** O(n²) on large or random data; many shifts for reversed input.

### Merge Sort
**Advantages:** guaranteed O(n log n); stable; great for large data and linked lists.
**Disadvantages:** needs O(n) extra memory; more overhead on small lists; recursive.

## When to Use Which

- **Small or nearly sorted data:** Insertion Sort
- **Large data, guaranteed performance:** Merge Sort
- **Learning and teaching:** Bubble Sort and Selection Sort
