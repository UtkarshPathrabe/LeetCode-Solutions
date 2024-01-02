# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def postOrder(node):
            nonlocal count
            if node == None:
                return (0, 0)
            leftSum, leftCount = postOrder(node.left)
            rightSum, rightCount = postOrder(node.right)
            nodeSum, nodeCount = leftSum + rightSum + node.val, leftCount + rightCount + 1
            if (nodeSum // nodeCount) == node.val:
                count += 1
            return (nodeSum, nodeCount)
        postOrder(root)
        return count