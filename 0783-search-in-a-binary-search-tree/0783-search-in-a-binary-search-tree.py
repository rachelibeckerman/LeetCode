# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        ### recursive solution:

        if(root == None):
            return None
        if(root.val == val):
            return root
        if(root.val > val):
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)


        # while(root != None):
        #     if(root.val == val):
        #         return root
        #     if(root.val > val):
        #         root = root.left
        #     else:
        #         root = root.right
        # else:
        #     return None
        