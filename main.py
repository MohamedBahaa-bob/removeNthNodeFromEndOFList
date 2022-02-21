# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        start = False
        count = 0
        preTarget = None
        while node is not None:
            if start:
                preTarget = preTarget.next
            if count == n:
                preTarget = head
                start = True
            node = node.next
            count += 1
        if preTarget is None:
            return head.next
        target = preTarget.next
        preTarget.next = target.next
        target.next = None
        return head


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
