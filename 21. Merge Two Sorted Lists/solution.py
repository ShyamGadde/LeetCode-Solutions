# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        sorted_list = None

        if list1.val < list2.val:
            sorted_list = list1
            list1 = list1.next
        else:
            sorted_list = list2
            list2 = list2.next

        tmp = sorted_list

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next

            tmp = tmp.next

        if list1:
            tmp.next = list1
        else:
            tmp.next = list2

        return sorted_list

# Time complexity: O(N)
# Space complexity: O(N)
