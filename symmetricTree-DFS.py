#Time Complexity: O(n)
#space Complexity: O(n); recursive stack space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):  
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

        
