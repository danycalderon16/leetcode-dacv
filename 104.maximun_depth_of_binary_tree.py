"""104. Maximum Depth of Binary Tree"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def to_string(self):
        """Helper method to visualize the tree structure."""
        lines = []
        self._print_tree(self, lines, "", "")
        return "\n".join(lines)
    
    def _print_tree(self, node, lines, prefix, is_tail):
        if node.right:
            new_prefix = prefix + ("│   " if is_tail else "    ")
            self._print_tree(node.right, lines, new_prefix, False)
        lines.append(prefix + ("└── " if is_tail else "┌── ") + str(node.val))
        if node.left:
            new_prefix = prefix + ("    " if is_tail else "│   ")
            self._print_tree(node.left, lines, new_prefix, True)
        
class Solution:

    def maxDepth(self,root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
if __name__ == "__main__":
    # Example usage:
    # Constructing the binary tree:
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    
    depth = solution.maxDepth(root)