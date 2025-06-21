class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Crea dos listas que comparten nodos a partir de 'intersect'
def build_intersected_lists(listA, listB, intersect):
    nodes = {}
    def build(values):
        head = ListNode(values[0]) if values else None
        curr = head
        for val in values[1:]:
            node = ListNode(val)
            curr.next = node
            curr = node
        return head

    headA = build(listA)
    headB = build(listB)
    inter_node = None
    if intersect:
        inter_node = build(intersect)
        # conectar A
        curr = headA
        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = inter_node
        else:
            headA = inter_node

        # conectar B
        curr = headB
        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = inter_node
        else:
            headB = inter_node

    return headA, headB, inter_node

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a

def print_list(head):
    values = []
    seen = set()
    while head and head not in seen:
        seen.add(head)
        values.append(head.val)
        head = head.next
    return values

if __name__ == "__main__":
    obj = Solution()

    # [4,1] -> [8,4,5]
    # [5,6,1] -> [8,4,5]
    headA, headB, inter = build_intersected_lists([4, 1], [5, 6, 1], [8, 4, 5])
    result = obj.getIntersectionNode(headA, headB)
    print("Intersection at:", result.val if result else None)
