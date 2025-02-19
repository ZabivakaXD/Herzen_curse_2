import unittest
from bin_tree import gen_bin_tree_line
from exception_bin_tree import *

class TestGenBinTreeRec(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(gen_bin_tree_line(height=3, root=1), {1: [{2: [{4: [8, 7]}, {5: [10, 8]}]}, {4: [{8: [16, 11]}, {7: [14, 10]}]}]})
        self.assertEqual(gen_bin_tree_line(height=1, root=5), {5: [10, 8]})
        self.assertEqual(gen_bin_tree_line(height=2, root=4), {4: [{8: [16, 11]}, {7: [14, 10]}]})

    def test_invalid_height_type(self):
        with self.assertRaises(BinaryTreeArgumentException):
            gen_bin_tree_line(height="3", root=1)

    def test_invalid_root_type(self):
        with self.assertRaises(BinaryTreeArgumentException):
            gen_bin_tree_line(height=3, root="1")

    def test_height_too_large(self):
        with self.assertRaises(BinaryTreeMemoryException):
            gen_bin_tree_line(height=32, root=1)

    def test_negative_height(self):
        with self.assertRaises(BinaryTreeIndexException):
            gen_bin_tree_line(height=-1, root=1)

if __name__ == '__main__':
    unittest.main()