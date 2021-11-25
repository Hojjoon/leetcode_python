from collections import deque


class MyQueue:

    # MyQueue 클래스 생성시 stk 변수 에 deque 생성후 저장  -->popleft()시에 O(1)연산이 가능하다. pop(0)하면 원소 하나씩 옆으로 땡겨야돼서  O(N)발생
    def __init__(self):
        self.stk = deque()

    # deque 의 append()를 이용해 원소를 맨 오른쪽에 추가
    def push(self, x: int) -> None:
        self.stk.append(x)

    # popleft() 를 이용해 맨 왼쪽 원소를 pop() 한 후 리턴한다. pop(0)보다 효율적임 (O(1)에 가능)
    def pop(self) -> int:
        return self.stk.popleft()

    # deque 의 맨 앞 인덱스를 반환 (queue 는 맨 앞의 값이, 즉 가장 먼저 들어간 값이 최상단 값, 즉 peek 값이다. )
    def peek(self) -> int:
        return self.stk[0]

    # deque 가 차 있으면 False, 그렇지 않으면 False 반환
    def empty(self) -> bool:
        if self.stk:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
