class BinaryTreeException(Exception):
    # def __init__(self, message = "BinaryTreeException raised occured"):
    #     super().__init__(message)
        
    def __str__(self):
        return "BinaryTreeException raised"
    
class BinaryTreeArgumentException(BinaryTreeException):
    def __str__(self):
        return "Argument of binary tree function is invalid"
    
class BinaryTreeRecursionException(BinaryTreeException):
    def __str__(self):
        return "Maximum recursion depth exceeded, reduce the height"

class BinaryTreeMemoryException(BinaryTreeException):
    def __str__(self):
        return "Out of memory"
    
class BinaryTreeIndexException(BinaryTreeException):
    def __str__(self):
        return "list assignment index out of range"