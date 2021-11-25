class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digs = []
        lets = []

        for log in logs:
            if log.split()[1].isdigit():
                digs.append(log)
            else:
                lets.append(log)

        # digs = sorted(digs)
        lets = sorted(lets, key=lambda x: (x.split()[1:], x.split()[0]))

        answer = lets + digs

        return answer