# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        # fill the inoder array with node values in in-order traversal
        self.inorder_traversal(root, inorder)

        #construct the balanced tree
        return self.create_b_tree(inorder, 0, len(inorder)-1)
    
    def inorder_traversal(self, root: TreeNode, inorder: list):
        # Perform an inorder traversal to store the elements in sorted order
        if not root:
            return
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)
    
    def create_b_tree(
        self, inorder: list, start: int, end: int
    ) -> TreeNode:
        # Base case: if the start index is greater than the end index, return None
        if start > end:
            return None

        # Find the middle element of the current range
        mid = start + (end - start) // 2

        # Recursively construct the left and right subtrees
        left_subtree = self.create_b_tree(inorder, start, mid - 1)
        right_subtree = self.create_b_tree(inorder, mid + 1, end)

        # Create a new node with the middle element and attach the subtrees
        node = TreeNode(inorder[mid], left_subtree, right_subtree)
        return node