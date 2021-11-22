class Solution:
    # 스택에 인덱스를 쌓아놓고 이전 값(스택 최상단 값)보다 큰 값을 만나면
    # 이전값 인덱스와 현재 인덱스(i)의 차이를 answer[이전값 인덱스]에 저장하고 stack.pop() 한다.
    # 이를 스택 최상단 값이 현재 비교대상 값 temperatures[i] 보다 작을동안 반복한다.

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)  # 이후 더 따뜻한 날 이 없으면 해당일은 답이 0이므로 굳이 0을 append 할 필요 없다. 모두 0으로 초기화 한다.
        stk = []  # 스택 선언

        for i in range(len(temperatures)):  # temperature를 순회하며 인덱스를 하나씩 저장해 나간다.
            while stk:  # 스택이 쌓여있는동안(있다면) 반복
                if temperatures[stk[-1]] < temperatures[i]:  # 스택 최상단값이 현재온도보다 작다면 현재온도 - 최상단값(인덱스)를 답에 저장 후 스택 pop()
                    answer[stk[-1]] = i - stk[-1]
                    stk.pop()
                else:  # 스택 최상단값이 현재온도보다 크거나 같다면 while 문 탈출 후
                    break
            stk.append(i)  # 스택에 i push()

        return answer

        # 처음에 스택에 인덱스 대신 온도값을 저장했더니 [89, 62, 70, 58, 47, 47, 46, 76, 100, 70] 와 같이
    # 47, 47, 이렇게 동일한 값이 있는 테스트케이스 에서는 답이 올바르게 안나왔다. (temperature 인덱스 접근시 건너뛰어버림)
    # 스택에 온도값 대신 인덱스를 저장하며 처리함으로써 문제를 해결할 수 있었다.

    # 결론 : 스택 사용시 값을 직접 저장하기보다는 인덱스를 저장하는것이 안전하다.
    # 배열 순회하며 더 큰값 or 작은값을 만나는 문제는 stack 이용해서 백트래킹 해본다.
