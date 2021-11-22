from collections import deque


class Solution:

    # 입력문자를 순차적으로 스택에 쌓는 과정에서
    # peek 괄호가 상대괄호를 만나면 peek 괄호를 stack 에서 pop()하는 방식
    # True 를 리턴하려면 모든 문자 순회 후 스택이 비어있어야 한다.
    # 스택이 비어있지 않으면 False 리턴
    # noinspection PyMethodMayBeStatic
    def is_valid(self, s: str) -> bool:

        if len(s) % 2 == 1:  # 괄호가 홀수개라면 True 가 될 수 없으므로 빠르게 False 리턴
            return False

        dic = {'(': ')', '[': ']', '{': '}'}  # 각 괄호의 시작과 끝을 dictionary 로 매칭 후 스택 선언
        stk = []

        for i in range(len(s)):  # 문자열 순회
            if stk and stk[-1] not in dic:  # 스택이 비어있지 않고 스택에 닫는 괄호가 하나라도 들어있다면 캐치해서 False 리턴
                return False
            elif stk and s[i] == dic[stk[-1]]:  # 스택이 비어있지 않고 현재 스택에 넣으려는 문자 s[i]가 스택의 peek 의 닫는괄호라면
                stk.pop()  # 스택 pop 후 continue
                continue
            stk.append(s[i])  # 스택 최상단에 문자 추가

        if stk:  # 문자열 순회 후 스택이 비어있지 않다면 False 리턴
            return False

        return True
