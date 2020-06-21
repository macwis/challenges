class MyQueue(object):
    def __init__(self):
        from collections import deque
        self.s1 = deque()
        self.s2 = deque()

    def put(self, value):
        self.s1.append(value)

    def prep(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self):
        self.prep()
        return self.s2.pop()

    def peek(self):
        self.prep()
        v = self.s2.pop()
        self.s2.append(v)
        return v


queue = MyQueue()

valtab = [
    [1, 42],
    [2],
    [1, 14],
    [3],
    [1, 28],
    [3],
    [1, 60],
    [1, 78],
    [2],
    [3],
    [2],
    [3],
    [2],
    [3]]
expected = [14, 14, 28, 60, 78]

act = []
for values in valtab:
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        act.append((queue.peek()))

if expected != act:
    print('Failed')
else:
    print('Passed')
