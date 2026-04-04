# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        streams = []

        def dfs(node):
            if node is None:
                streams.append("N")
                return
            
            streams.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(streams)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0
        def dfs():
            if values[self.i] == "N":
                return None
            
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            self.i += 1
            node.right = dfs()

            return node
        
        root = dfs()
        return root

