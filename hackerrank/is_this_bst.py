class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
            self.nodes.append(self.root)
        else:
            current = self.root

            while True:
                if val <= current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


u = []
def scan(node):
    if node.data:
        if node.left:
            checkBST(node.left)
        u.append(node.data)
        if node.right:
            checkBST(node.right)
        return u

def checkBST(root):
    messedup_u = scan(root)
    # set checks uniquenes
    # sorted checks the order
    return sorted(list(set(messedup_u))) == messedup_u



if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(checkBST(tree.root))
