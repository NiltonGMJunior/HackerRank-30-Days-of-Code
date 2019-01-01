class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
                start = head
                while(start.next is not None):
                    start = start.next
                start.next = p
            return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        while True:
            current = head
            data = [head.data]
            any_removed = False
            while current.next:
                if current.next.data not in data:
                    data.append(current.next.data)
                else:
                    any_removed = True
                    if current.next.next:
                        current.next = current.next.next
                    else:
                        current.next = None
                        break
                current = current.next
            if any_removed:
                continue
            else:
                break

        return head


# mylist = Solution()
# T = int(input())
# head = None
# for i in range(T):
#     data = int(input())
#     head = mylist.insert(head, data)
# head = mylist.removeDuplicates(head)
# mylist.display(head)

mylist = Solution()
T = 6
head = None
for i in [1, 2, 2, 3, 3, 4]:
    data = i
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)

# mylist = Solution()
# T = 7
# head = None
# for i in [1, 1, 1, 1, 1, 1, 1]:
#     data = i
#     head = mylist.insert(head, data)
# head = mylist.removeDuplicates(head)
# mylist.display(head)
