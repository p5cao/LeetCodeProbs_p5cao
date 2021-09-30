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
// C++ solution1 breadth-first-search using queue
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int count = 0;        
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            count++;
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode *cur = q.front();
                q.pop();
                if (cur->left) q.push(cur->left);                    
                if (cur->right) q.push(cur->right);
            }
    }        
    return count;
    }
};
