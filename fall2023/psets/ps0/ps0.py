#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    sum = 1 # Root is included in size

    if v.left is not None:
        sum += calculate_sizes(v.left)
    if v.right is not None:
        sum += calculate_sizes(v.right)
    
    v.size = sum
    return sum

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):
    n = r.size
    current_vertex = r

    while True:
        left_size, right_size = 0, 0;

        if current_vertex.left is not None:
            left_size = current_vertex.left.size
        if current_vertex.right is not None:
            right_size = current_vertex.right.size
        parent_size = n - left_size - right_size - 1

        if max(left_size, right_size, parent_size) <= n // 2:
            return current_vertex
        
        if left_size > n // 2:
            current_vertex = current_vertex.left
        elif right_size > n // 2:
            current_vertex = current_vertex.right