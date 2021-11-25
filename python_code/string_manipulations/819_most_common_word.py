import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        discovered = {}
        paragraph = re.sub(r'[^\w]', ' ', paragraph).lower().split()

        for word in paragraph:
            if word not in banned:
                if word not in discovered:
                    discovered[word] = 1
                else:
                    discovered[word] += 1

        answer = max(discovered, key=lambda x: discovered[x])

        return answer