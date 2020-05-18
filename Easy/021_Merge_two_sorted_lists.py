# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = head = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                n.next = l2
                l2 = l2.next
            else:
                n.next = l1
                l1 = l1.next
            n = n.next
        if l1:
            n.next = l1
        if l2:
            n.next = l2            
        return head.next
        
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
