# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert(val)
      
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

if __name__ == "__main__":
    head = ListNode(1)
    head.insert(2)
    head.insert(4)
    print(head)