import unittest

from disjoint_set import DisjointSet

class TestDisjointSet(unittest.TestCase):
    def test_initialization(self):
        """
        Test that the disjoint-set is initialized correctly.
        """
        size = 5
        ds = DisjointSet(size)

        # Each element should be its own parent initially
        for i in range(size):
            self.assertEqual(ds.find(i), i)

        # Ranks should all be 1 initially
        self.assertEqual(ds.rank, [1] * size)

    def test_union_and_connected(self):
        """
        Test the union and connected operations.
        """
        ds = DisjointSet(10)

        # Initially, no elements are connected
        self.assertFalse(ds.connected(1, 2))
        self.assertFalse(ds.connected(3, 4))

        # Union some elements
        ds.union(1, 2)
        ds.union(3, 4)
        ds.union(1, 3)

        # Check connections
        self.assertTrue(ds.connected(1, 2))
        self.assertTrue(ds.connected(3, 4))
        self.assertTrue(ds.connected(1, 4))  # Transitive connection
        self.assertFalse(ds.connected(1, 5))  # Not connected

    def test_path_compression(self):
        """
        Test that path compression works in the find operation.
        """
        ds = DisjointSet(10)

        # Create a deep tree
        ds.union(1, 2)
        ds.union(2, 3)
        ds.union(3, 4)

        # Before path compression, the parent of 4 is 3
        self.assertEqual(ds.find(4), 1)  # Path compression flattens the tree

        # After path compression, the parent of 4 should directly point to the root (1)
        self.assertEqual(ds.parent[4], 1)

    def test_union_by_rank(self):
        """
        Test that union by rank keeps the tree balanced.
        """
        ds = DisjointSet(10)

        # Union smaller trees under larger trees
        ds.union(1, 2)  # Rank of 1 becomes 2
        ds.union(3, 4)  # Rank of 3 becomes 2
        ds.union(1, 3)  # Rank of 1 becomes 3 (since ranks are equal)

        # Check ranks
        self.assertEqual(ds.rank[1], 3)
        self.assertEqual(ds.rank[3], 2)

    def test_large_disjoint_set(self):
        """
        Test the disjoint-set with a large number of elements.
        """
        size = 1000
        ds = DisjointSet(size)

        # Union all even elements and all odd elements
        for i in range(0, size - 2, 2):
            ds.union(i, i + 2)
        for i in range(1, size - 1, 2):
            ds.union(i, i + 2)

        # Check connections
        self.assertTrue(ds.connected(0, size - 2))  # All even elements connected
        self.assertTrue(ds.connected(1, size - 1))  # All odd elements connected
        self.assertFalse(ds.connected(0, 1))        # Even and odd elements not connected
