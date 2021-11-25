class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * (k + 1)
        self.front = 0
        self.rear = 0

    # noinspection PyMethodMayBeStatic
    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        else:
            self.rear += 1
            self.cq[self.rear % len(self.cq)] = value
            return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.cq[(self.front + 1) % len(self.cq)] = None
            self.front += 1
            return True

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.cq[(self.front + 1) % len(self.cq)]

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.cq[self.rear % len(self.cq)]

    def is_empty(self) -> bool:
        if self.front == self.rear:
            return True
        return False

    def is_full(self) -> bool:
        if (self.rear + 1) % len(self.cq) == self.front:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enqueue(value)
# param_2 = obj.dequeue()
# param_3 = obj.front()
# param_4 = obj.fear()
# param_5 = obj.is_empty()
# param_6 = obj.is_full()
