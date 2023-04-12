# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        move = dummy
        #list1和list2为两个链表的头结点，在后面操作中进行了改变
        while list1 and list2:
            if list1.val <= list2.val:
                move.next = list1
                list1 = list1.next
            else:
                move.next = list2
                list2 = list2.next
            move = move.next
        if list1:
            move.next = list1
        else:
            move.next = list2
        return dummy.next
