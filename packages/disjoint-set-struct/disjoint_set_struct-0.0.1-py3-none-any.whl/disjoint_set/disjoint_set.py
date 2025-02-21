class DisjointSet:
    """
    A disjoint-set (union-find) data structure for managing a collection of disjoint sets.

    This data structure supports two main operations:
    - `find`: Determine which subset a particular element is in.
    - `union`: Join two subsets into a single subset.

    The implementation uses two optimizations:
    - **Path compression**: Flattens the structure of the tree during `find` operations.
    - **Union by rank**: Attaches the smaller tree to the root of the larger tree during `union` operations.

    Attributes:
        parent (list[int]): A list where each element points to its parent in the set.
        rank (list[int]): A list representing the rank (approximate depth) of each set.
    """
    def __init__(self, size: int) -> None:
        """
        Initialize the disjoint-set data structure.

        Args:
            size (int): The number of elements in the disjoint-set. Each element is initially its own parent.
        """
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        """
        Find the root of the set containing the element `x`.

        This method applies path compression to flatten the tree, making future queries faster.

        Args:
            x (int): The element whose root is to be found.

        Returns:
            int: The root of the set containing `x`.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Union the sets containing elements `x` and `y`.

        This method uses union by rank to attach the smaller tree to the root of the larger tree.

        Args:
            x (int): The first element.
            y (int): The second element.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Check if elements `x` and `y` are in the same set.

        Args:
            x (int): The first element.
            y (int): The second element.

        Returns:
            bool: `True` if `x` and `y` are in the same set, `False` otherwise.
        """
        return self.find(x) == self.find(y)
