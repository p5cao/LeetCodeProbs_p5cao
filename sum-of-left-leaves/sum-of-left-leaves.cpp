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
    
    void helper(TreeNode* root, int& sum, bool is_left){
        if(root == NULL){ 
            return; // end if root is null
        }
        
        if(root->left==NULL && root->right==NULL){
            if(is_left){
                sum+=root->val;
            }
            return;
        }
        helper(root->left, sum, true);
        helper(root->right, sum, false);
    }
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == NULL||(root->left==NULL && root->right==NULL)){
            return 0;
        }
        int sum = 0;
        helper(root, sum, true);
        return sum;
    }
};