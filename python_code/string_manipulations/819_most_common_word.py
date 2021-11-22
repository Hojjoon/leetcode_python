import re


class Solution:
    # noinspection PyMethodMayBeStatic
    def most_common_word(self, paragraph: str, banned: list) -> str:
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
