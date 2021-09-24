# 1669. Merge In Between Linked Lists
# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        curr = list1
        for i in range(0, a - 1):
            curr = curr.next

        a_node = curr.next
        curr.next = list2

        curr = a_node
        for i in range(a, b):
            curr = curr.next

        curr2 = list2
        while curr2.next is not None:
            curr2 = curr2.next
        curr2.next = curr.next

        return list1