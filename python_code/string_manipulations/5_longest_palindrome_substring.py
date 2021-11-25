from collections import deque


class Solution:
    def is_palindrome(self, str1: str) -> bool:

        deq = deque(str1)

        while deq:
            if len(deq) == 1:
                return True
            if deq.pop() != deq.popleft():
                return False
        return True

    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1 or len(s) == 0:
            return s

        discovered = []

        for i in range(2, len(s) + 1):
            left = 0
            while i < len(s) + 1:
                if self.is_palindrome(s[left:i]) and s[left:i] not in discovered:
                    discovered.append(s[left:i])
                left += 1
                i += 1
        if len(discovered) == 0:
            answer = s[0]
        else:
            answer = max(discovered, key=len)

        return answer
