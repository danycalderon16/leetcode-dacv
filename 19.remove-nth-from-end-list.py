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

    def length(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next

        return count

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer ahead by n+1 steps
        for i in range(n+1):
            first = first.next
        
        # Move both pointers simultaneously until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Now the second pointer points to the node just before the node to be deleted
        second.next = second.next.next
        
        return dummy.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        

if __name__ == '__main__':
    head = ListNode(1)

    head.insert(2)
    head.insert(3)
    head.insert(4)
    head.insert(5)
    head.removeNthFromEnd(head,2)

    # res = Solution().removeNthFromEnd()