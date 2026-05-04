# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

        def serialize(self, root):
            result = []
            def dfs(node):
                if node is None:
                    result.append("null")
                    return 
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return ",".join(result)
        def deserialize(self,data):
            values = data.split(",")
            index = [0]
            def build():
                if values[index[0]] == "null":
                    index[0] = index[0]+1
                    return None
                node = TreeNode(int(values[index[0]]))
                index[0] = index[0] +1
                node.left = build()
                node.right = build()
                return node
            return build()
                
                                                                                                                                 
                                                                                                                                                                                                                
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))