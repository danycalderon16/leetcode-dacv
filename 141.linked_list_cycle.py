class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Construcción especial para crear ciclo
def build_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None if pos == -1 else head if pos == 0 else None
    for idx, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if idx == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head: return False
        turtle = head
        hare = head.next
        
        while hare and hare.next:
            if hare == turtle:
                return True
            turtle = turtle.next
            hare = hare.next.next
            
        return False

if __name__ == "__main__":
    obj = Solution()

    tests = [
        ([1,2], -1),   # ciclo en nodo con valor 2
        ([1, 2], 0),          # ciclo al nodo 1
        ([1], -1),            # sin ciclo
        ([], -1),             # lista vacía
    ]

    for i, (vals, pos) in enumerate(tests):
        head = build_linked_list_with_cycle(vals, pos)
        result = obj.hasCycle(head)
        print(f"Test case {i + 1}: Input: {vals} with cycle at {pos} => Output: {result}")
