# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        deq = deque()

        # 노드에 값이 없으면 True 반환
        if not head:
            return True

        node = head

        # 연결된 노드가 없을때까지 반복
        while node is not None:
            deq.append(node.val)
            node = node.next

        # 데크를 이용하여 팰린드롬 판별
        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False

        return True