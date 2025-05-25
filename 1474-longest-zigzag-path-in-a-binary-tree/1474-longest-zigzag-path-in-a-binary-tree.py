# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val,
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        self.dfs(root,'l',0)
        # self.dfs(root,'r',0)
        return self.maxLength
    
    def dfs(self, node, direction,length) :
        if not node:
            return

        self.maxLength = max(self.maxLength,length)
        if direction == 'l':
            self.dfs(node.left,'r',length+1)
            self.dfs(node.right,'l',1)
        else:
            self.dfs(node.right,'l',length+1)
            self.dfs(node.left,'r',1)
        

        
        
    