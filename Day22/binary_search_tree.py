class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        max_height = 0
        nodes = [root]
        while True:
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)

            nodes = new_nodes
            if nodes:
                max_height += 1
            else:
                break

        return max_height


# T = int(input())
# myTree = Solution()
# root = None
# for i in range(T):
#     data = int(input())
#     root = myTree.insert(root, data)
# height = myTree.getHeight(root)
# print(height)

T = 7
myTree = Solution()
root = None
for i in [3, 5, 2, 1, 4, 6, 7]:
    data = i
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)

# T = 9
# myTree = Solution()
# root = None
# for i in [20, 50, 35, 44, 9, 15, 62, 11, 13]:
#     data = i
#     root = myTree.insert(root, data)
# height = myTree.getHeight(root)
# print(height)
