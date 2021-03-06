class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            return head
        else:
            return new_node


# mylist = Solution()
# T = int(input())
# head = None
# for i in range(T):
#     data = int(input())
#     head = mylist.insert(head, data)
# mylist.display(head)

mylist = Solution()
T = int("4")
head = None
inp = ["2", "3", "4", "1"]
for i in range(T):
    data = int(inp[i])
    head = mylist.insert(head, data)
mylist.display(head)
