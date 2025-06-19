class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution(object):
    def deleteDuplicates(self, head:ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        start = head
        
        while head and head.next:
            if head.val == head.next.val: 
                head.next = head.next.next
            else:
                head = head.next
        
        return start

if __name__ == "__main__":
    obj = Solution()

    test_cases = [
        [1, 1, 1],
        [1, 1, 2, 3, 3],
        [1, 2, 3],
        [1, 1, 1],
        [],
        [1],
    ]

    for i, input_list in enumerate(test_cases):
        head = build_linked_list(input_list)
        new_head = obj.deleteDuplicates(head)
        print(f"Test case {i + 1}: Input: {input_list} => Output: {linked_list_to_list(new_head)}")
