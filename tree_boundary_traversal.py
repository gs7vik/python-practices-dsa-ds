# Uncomment or define this Node class in your file
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def boundaryTraversal(self, root):
        # helper to collect left boundary (excluding leaves)
        def traverseLeft(node, ans):
            if node is None or (node.left is None and node.right is None):
                return
            ans.append(node.data)
            if node.left:
                traverseLeft(node.left, ans)
            else:
                traverseLeft(node.right, ans)

        # helper to collect all leaves (left -> right)
        def traverseLeaf(node, ans):
            if node is None:
                return
            if node.left is None and node.right is None:
                ans.append(node.data)
                return
            traverseLeaf(node.left, ans)
            traverseLeaf(node.right, ans)

        # helper to collect right boundary (excluding leaves) in reverse order
        def traverseRight(node, ans):
            if node is None or (node.left is None and node.right is None):
                return
            # go deep first so we can add on return (reverse order)
            if node.right:
                traverseRight(node.right, ans)
            else:
                traverseRight(node.left, ans)
            ans.append(node.data)

        ans = []
        if root is None:
            return ans

        # root
        ans.append(root.data)

        # left boundary (excluding leaves)
        traverseLeft(root.left, ans)

        # all leaf nodes
        traverseLeaf(root.left, ans)
        traverseLeaf(root.right, ans)

        # right boundary (excluding leaves), added in reverse by traverseRight
        traverseRight(root.right, ans)

        return ans
