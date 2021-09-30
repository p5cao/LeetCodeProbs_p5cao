class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int depth = 0;
		// use single linked list to store the next row of nodes, initialized with just the root
        forward_list<TreeNode*> nodes(1, root);
        while (!nodes.empty()) {
			// add one to the depth because this marks the start of a new row of nodes
            depth++;
			// another linked list to store the upcoming row while we traverse the current row
            forward_list<TreeNode*> nextRow;
            for (TreeNode* node : nodes) {
                if (node->left) {
                    nextRow.push_front(node->left);
                }
                if (node->right) {
                    nextRow.push_front(node->right);
                }
            }
            nodes = nextRow;
        }
        
        return depth;
    }
};