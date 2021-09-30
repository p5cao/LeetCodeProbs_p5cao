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
// C++ solution1 breadth-first-search using forward_list
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int level = 0;
        if (!root) return level;
        forward_list<TreeNode*> node_list (1,root);
        
        while (!node_list.empty()){
            level ++;
            forward_list<TreeNode*> new_list;
            for(TreeNode* node : node_list){
                if(node->left){
                    new_list.push_front(node->left);
                }
                if(node->right){
                    new_list.push_front(node->right);
                } 
            }
            node_list = new_list;
        }
        
        return level;
    }
};
