from collections import deque


class Solution:
    # noinspection PyMethodMayBeStatic
    def is_palindrome(self, s: str) -> bool:

        a = ''.join(i for i in s if i.isalnum()).lower()
        deq = deque(list(a))

        if len(deq) == 0:
            return True

        while len(deq) >= 0:
            if 2 > len(deq):
                return True
            if deq.popleft() != deq.pop():
                return False