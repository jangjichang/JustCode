# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return 0


def test_solution():
    solution = Solution()
    assert solution.mergeTwoLists(ListNode(), ListNode()) == 1
