/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) 
    {
        return buildBST(preorder, 0, preorder.length);
    }

    private TreeNode buildBST(int[] preorder, int start, int end) {
        if(start >= end) {
            return null;
        }
        int rootval = preorder[start];
        TreeNode root = new TreeNode(rootval);

        // Find the first index of element greater than root
        int i = start + 1;
        while(i < end && preorder[i] < rootval) {
            i++;
        }
        root.left = buildBST(preorder, start + 1, i);
        root.right = buildBST(preorder, i, end);
        return root;
    }
}
