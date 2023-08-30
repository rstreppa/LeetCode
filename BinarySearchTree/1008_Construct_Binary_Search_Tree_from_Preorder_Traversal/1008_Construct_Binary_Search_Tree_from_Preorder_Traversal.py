# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode

        1008. Construct Binary Search Tree from Preorder Traversal
        Medium
        Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), 
        construct the tree and return its root.

        It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

        A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val,
        and any descendant of Node.right has a value strictly greater than Node.val.

        A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

        Example 1:
        Input: preorder = [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]
        
        Example 2:
        Input: preorder = [1,3]
        Output: [1,null,3]
        """

        # In a BST constructed from a preorder array, the sequence is as follows:

        # 1 The first element is the root.
        # 2 The elements that follow, which are smaller than the root, are all nodes in the left subtree.
        # 3 The remaining elements are all nodes in the right subtree.

        # I've used two pointers, start and end, to keep track of the segment of the preorder array that we're currently considering 
        # for each subtree. This eliminates the need to slice the array, reducing extra time and space complexity.

        def buildBST(preorder, start, end):
            if start >= end:
                return None
            
            rootval = preorder[start]
            root = TreeNode(val=rootval)
            
            # Find the first index of element greater than root
            i = start + 1
            while i < end and preorder[i] < rootval:
                i += 1
            
            root.left = buildBST(preorder, start + 1, i)
            root.right = buildBST(preorder, i, end)
            
            return root

        return buildBST(preorder, 0, len(preorder))
