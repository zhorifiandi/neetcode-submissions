# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # construct parent pointers, and calculate p and q depth
        parent = {root: None}
        stack = [(root, 1)]
        p_depth = q_depth = None
        
        while stack:
            node, depth = stack.pop()

            if node is None:
                continue
            
            if node.val == p.val:
                p = node
                p_depth = depth
            
            if node.val == q.val:
                q = node
                q_depth = depth
            
            if p_depth is not None and q_depth is not None:
                break
            
            if node.left:
                stack.append((node.left, depth + 1))
                parent[node.left] = node
            
            if node.right:
                stack.append((node.right, depth + 1))
                parent[node.right] = node


        # which ever node has bigger depth, move upward
        # if depth same, move both
        # whenever we found same node, it's the lca
        while p and q:
            if p == q:
                return p
            
            if p_depth > q_depth:
                p = parent[p]
                p_depth -= 1
            elif p_depth < q_depth:
                q = parent[q]
                q_depth -= 1
            else:
                p = parent[p]
                p_depth -= 1
                q = parent[q]
                q_depth -= 1

        return None