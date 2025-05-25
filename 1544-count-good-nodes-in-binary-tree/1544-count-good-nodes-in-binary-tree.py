# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numOfGoodNoodes = 0
        self.dfs(root,root.val)
        return self.numOfGoodNoodes


    def dfs(self, node:TreeNode ,maxValue:int):
        if not node:
            return 
        if maxValue <= node.val:
            self.numOfGoodNoodes += 1
            maxValue = node.val
        self.dfs(node.left,maxValue)
        self.dfs(node.right,maxValue)
        
            

        