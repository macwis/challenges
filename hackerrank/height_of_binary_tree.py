class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

from collections import deque

def height(root):
    q = deque()
    visited = {k: False for k in range(1, 21)}
    dist = {k: 0 for k in range(1, 21)}
    visited[root.info] = True
    q.append(root)
    c = 1
    while q:
        v = q.pop()
        if v.left and not visited[v.left.info]:
            visited[v.left.info]
            q.append(v.left)
            dist[v.left.info] = dist[v.info] + 1
        if v.right and not visited[v.right.info]:
            visited[v.right.info]
            q.append(v.right)
            dist[v.right.info] = dist[v.info] + 1
    return max(dist.values())


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))
