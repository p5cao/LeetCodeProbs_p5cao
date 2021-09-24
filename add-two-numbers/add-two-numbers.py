# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        ptr = dummy_node
        carry = 0
        
        while l1 or l2 or carry:
            # edge case 7+8 = 15, both next nodes are zeros but carry = 1
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            
            carry = val // 10
            val = val % 10
            ptr.next = ListNode(val)
            
            # update ptrs
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_node.next
            