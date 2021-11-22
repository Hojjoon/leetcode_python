from collections import deque


class MyStack:

    # MyStack 생성시 deque 를 생성하여 변수 q에 저장한다.
    def __init__(self):
        self.q = deque()

    # deque 의 오른쪽 끝에 x를 append 한다.
    def push(self, x: int) -> None:
        self.q.append(x)

    # deque 의 맨 오른쪽 값을 pop() 하여 리턴한다.
    def pop(self) -> int:
        return self.q.pop()

    # deque 의 맨 오른쪽 값을 리턴한다
    def top(self) -> int:
        return self.q[-1]

    # deque 가 비어있다면 True, 차있다면 False 리턴한다.
    def empty(self) -> bool:
        if self.q:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
