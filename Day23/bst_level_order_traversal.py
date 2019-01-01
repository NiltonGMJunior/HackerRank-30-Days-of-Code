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

    def levelOrder(self, root):
        print_output = [root.data]
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
                for node in nodes:
                    print_output.append(node.data)
            else:
                break

        print(" ".join(map(str, print_output)))


# T = int(input())
# myTree = Solution()
# root = None
# for i in range(T):
#     data = int(input())
#     root = myTree.insert(root, data)
# myTree.levelOrder(root)

T = 6
myTree = Solution()
root = None
for i in [3, 5, 4, 7, 2, 1]:
    data = i
    root = myTree.insert(root, data)
myTree.levelOrder(root)
