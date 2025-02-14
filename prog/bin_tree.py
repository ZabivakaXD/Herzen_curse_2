from exception_bin_tree import *
import unittest

def gen_bin_tree_rec(height = 3, root = 1):
    if type(height) is not int or type(root) is not int:
        raise BinaryTreeArgumentException()
    elif height > 995 or height < 0:
        raise BinaryTreeRecursionException()
    else:
        feed = {}
        left_leaf = root * 2
        right_leaf = root + 3
        
        if height != 1:
            left_branch = gen_bin_tree_rec(height - 1, left_leaf)
            right_branch = gen_bin_tree_rec(height - 1, right_leaf)
        if height == 1:
            feed[root] = [left_leaf, right_leaf]
        else:
            feed[root] = [left_branch, right_branch]

    return feed

def gen_bin_tree_line(height = 3, root = 1):
    if type(height) is not int or type(root) is not int:
        raise BinaryTreeArgumentException()
    elif height > 31:
        raise BinaryTreeMemoryException()
    elif height < 0:
        raise BinaryTreeIndexException()
    else:
        numbers = [0] * (2**(height + 1) - 1)
        count = 0
        numbers[count] = root
        
        while count * 2 + 1 <= len(numbers) - 1:  
            numbers[count * 2 + 1] = numbers[count] * 2 
            if count * 2 + 2 <= len(numbers) - 1:  
                numbers[count * 2 + 2] = numbers[count] + 3
            count += 1
            
        for height_local in range (height, 0, -1):
            lvl_down = numbers[2**height_local - 1:len(numbers)]
            lvl_up = numbers[2**(height_local - 1) - 1:len(numbers) - 2**height_local]
            numbers.reverse()
            del numbers[0:2**height_local + 2**(height_local - 1)]
            # for deleter in range(0, 2**height_local + 2**(height_local - 1)):
            #     numbers.pop(0)
            numbers.reverse()
            count = 0
            while count < len(lvl_up):
                numbers.append({lvl_up[count] : [lvl_down[count * 2], lvl_down[count * 2 + 1]]})
                count += 1
            
    return numbers[0]
    
class TestGenBinTreeRec(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(gen_bin_tree_rec(height=3, root=1), {1: [{2: [{4: [8, 7]}, {5: [10, 8]}]}, {4: [{8: [16, 11]}, {7: [14, 10]}]}]})
        self.assertEqual(gen_bin_tree_rec(height=1, root=5), {5: [10, 8]})
        self.assertEqual(gen_bin_tree_rec(height=2, root=4), {4: [{8: [16, 11]}, {7: [14, 10]}]})

    def test_invalid_height_type(self):
        with self.assertRaises(BinaryTreeArgumentException):
            gen_bin_tree_rec(height="3", root=1)

    def test_invalid_root_type(self):
        with self.assertRaises(BinaryTreeArgumentException):
            gen_bin_tree_rec(height=3, root="1")

    def test_height_too_large(self):
        with self.assertRaises(BinaryTreeRecursionException):
            gen_bin_tree_rec(height=996, root=1)

    def test_negative_height(self):
        with self.assertRaises(BinaryTreeRecursionException):
            gen_bin_tree_rec(height=-1, root=1)

def main():
    tree_rec = gen_bin_tree_rec()
    print(tree_rec)
    # tree_line = gen_bin_tree_line()
    # print(tree_line)
    
if __name__ == '__main__':
    # main()
    unittest.main()