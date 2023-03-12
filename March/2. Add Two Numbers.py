#Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = linkedList = ListNode()
        val = up = 0
        while up or l1 or l2:
            val = up
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            up = val // 10
            val = val % 10
            linkedList.next = ListNode(val)
            linkedList = linkedList.next

        return head.next
