# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0)
        dummy2 = dummy
        dummy.next = head
        temp = dummy.next
        while temp:
            if temp.val in nums:
                dummy.next = temp.next
                temp.next = None
                temp = dummy.next
            else:
                dummy = temp
                temp = temp.next
        return dummy2.next