"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sintinel = head
        oddTail = head
        if sintinel is None:
            return sintinel
        evenHead = head.next
        evenTail = head.next
        if evenHead is None:
            return sintinel
        next = head.next.next
        while True:
            if next is None:
                oddTail.next = evenHead
                return sintinel
            elif evenTail.next == next:
                oddTail.next = next
                oddTail = oddTail.next
                evenTail.next = None
            elif oddTail.next == next:
                evenTail.next = next
                evenTail = evenTail.next
                oddTail.next = None
            next = next.next



if __name__ == "__main__":
    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    s = Solution()
    s.oddEvenList(node1)

    node = node1
    while True:
        print(node.val, end=" ")
        if node.next is None:
            break
        node = node.next

