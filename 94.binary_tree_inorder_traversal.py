# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(root, result)
        return result


    def inorder(self, root,result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
        return result
    
if __name__ == "__main__":

  res = Solution().inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3))))

  print(res)  