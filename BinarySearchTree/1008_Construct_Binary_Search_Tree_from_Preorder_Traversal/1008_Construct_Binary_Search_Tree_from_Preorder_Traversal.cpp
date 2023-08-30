/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) 
    {
        return buildBST(preorder, 0, preorder.size());   
    }
private:
    TreeNode* buildBST(vector<int>& preorder, size_t start, size_t end) 
    {
        if(start >= end)
            return nullptr;
        
        int rootval = preorder[start];
        TreeNode* root = new TreeNode(rootval);

        // Find the first index of element greater than root
        size_t i = start + 1;
        while( i < end && preorder[i] < rootval)
            i++;
        root->left  = buildBST(preorder, start+1, i);
        root->right = buildBST(preorder, i, end);

        return root;
    }
};
