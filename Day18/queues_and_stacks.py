import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        self.stack.append(char)

    def enqueueCharacter(self, char):
        self.queue += [char]

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        first_char = self.queue[0]
        self.queue = self.queue[1:]
        return first_char


# Read the string s
# s = input()
s = "test"
# Create the Solution class object
obj = Solution()

l = len(s)

# Push/enqueue all the characters of string s to stack

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])


isPalindrome = True

'''
Pop the top character from stack
Dequeue the first character from queue
Compare both the characters
'''

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Finally print whether string s is palindrome or not.

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
