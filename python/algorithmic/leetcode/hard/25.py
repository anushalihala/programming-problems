# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(head, k, i):
            if i == k:
                # print(head.val)
                remaining_list = head.next
                head.next = None
                return [head, head, remaining_list]

            this_list_head, this_list_tail, remaining_list = reverseK(head.next, k, i + 1)
            head.next = None
            this_list_tail.next = head
            return [this_list_head, head, remaining_list]

        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        groups = length // k

        new_list_head = head
        for i in range(groups):
            curr_list_head, curr_list_tail, remaining_list = reverseK(head, k, 1)
            # print(curr_list_head, curr_list_tail, remaining_list)
            head = remaining_list

            if i == 0:
                new_list_head = curr_list_head
                prev_tail = curr_list_tail
            else:
                prev_tail.next = curr_list_head
                prev_tail = curr_list_tail
        prev_tail.next = remaining_list
        return new_list_head

# 1 2 3 4 5
#     p
#     3->None
#     3, 4 5
# 2:    3, 4 5
#      2->None
#      3->2
#      3 2, 4 5
# 1:    1->None
#      3->2->1
#      3 2 1, 4 5

