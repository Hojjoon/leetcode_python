class Solution:
    # noinspection PyMethodMayBeStatic
    def group_anagrams(self, strs: list) -> list[list]:

        dic1 = {}

        for i in strs:
            if ''.join(sorted(list(i))) not in dic1:
                dic1[''.join(sorted(list(i)))] = [i]
            else:
                dic1[''.join(sorted(list(i)))].append(i)

        answer = list(dic1.values())

        return answer
