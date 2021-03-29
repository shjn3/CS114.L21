import collections

class Node:
    def __init__(self,data=None,left =None,right = None):
        self.data = data
        self.right = left
        self.left = right
    def addNode(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.addNode(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.addNode(data)
        else:
            self.data = data
def BSF(root):
    if root is None:
        return 
    mo = []
    mo.append(root)
    while mo:
        s = mo.pop()
        print(s.data,end=" ")
        if s.left is None and s.right is None:
            continue
        if s.left is not None and s.right is not None:
            mo.insert(0,s.left)
            mo.insert(0,s.right)
        elif s.left is None:
            mo.insert(0,s.right)
        elif s.right is None:
            mo.insert(0,s.left)

a = Node()
while True:
    q = int(input())
    if q == 0:
        BSF(a)
        break
    a.addNode(q)
