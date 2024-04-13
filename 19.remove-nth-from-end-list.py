# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
      
    def insert(self, val):
        current = self
        while current.next is not None:
            current = current.next
        current.next = ListNode(val)
    
    def print(self):
        current = self
        while current is not None:
            print(current.val)
            current = current.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        

if __name__ == '__main__':
    head = ListNode(234)

    head.insert(1)
    head.print()

    # res = Solution().removeNthFromEnd()