# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.answer = []

        def traverse(node, depth):
            if node is None:
                return
            
            if len(self.answer) <= depth:
                self.answer.append([])
            
            self.answer[depth].append(node.val)
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)
        return self.answer