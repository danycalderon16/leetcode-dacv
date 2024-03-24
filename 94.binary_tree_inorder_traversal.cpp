#include <iostream>
#include <vector>
#include <stack>

using namespace std;
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution{
public:
    vector<int> inorderTraversal(TreeNode *root) {
    }
};


    int main() {
         Solution solution;

    // Creating a binary tree
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // Calling inorderTraversal and printing the result
    vector<int> inorder = solution.inorderTraversal(root);
    cout << "Inorder traversal: ";
    for (int val : inorder) {
        cout << val << " ";
    }
    cout << endl;

    // Clean up the memory allocated for the tree nodes
    // Add cleanup code if necessary

    return 0;
    }