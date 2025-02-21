# Disjoint Set (Union-Find) Data Structure

This repository contains a Python implementation of the **Disjoint Set** (also known as **Union-Find**) data structure. The implementation includes optimizations such as **path compression** and **union by rank** to ensure efficient operations.

## Features
- **Find**: Determine the root of the set containing a given element.
- **Union**: Merge two sets into one.
- **Connected**: Check if two elements are in the same set.
- **Path Compression**: Flattens the tree during `find` operations for faster future queries.
- **Union by Rank**: Keeps the tree balanced by attaching smaller trees to larger ones.

## Code Overview

### `DisjointSet` Class

#### Attributes
- **`parent`**: A list where each element points to its parent in the set.
- **`rank`**: A list representing the rank (approximate depth) of each set.

#### Methods
- **`__init__(size: int)`**: Initializes the disjoint-set with `size` elements.
- **`find(x: int) -> int`**: Finds the root of the set containing `x` with path compression.
- **`union(x: int, y: int)`**: Merges the sets containing `x` and `y` using union by rank.
- **`connected(x: int, y: int) -> bool`**: Checks if `x` and `y` are in the same set.

### Example Usage

```python
# Create a disjoint-set with 10 elements
ds = DisjointSet(10)

# Perform some union operations
ds.union(1, 2)
ds.union(3, 4)
ds.union(1, 3)

# Check if elements are connected
print(ds.connected(1, 4))  # Output: True
print(ds.connected(1, 5))  # Output: False