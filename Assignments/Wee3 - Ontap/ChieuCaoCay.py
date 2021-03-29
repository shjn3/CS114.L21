from sys import stdin
import collections

class Node:
    def __init__(self,data=None,left =None,right = None):
        self.data = data
        self.right = left
        self.left = right

    def addNode(self,data):
        if self.data is not None:
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

    def chieucao(self,root):
        if root is None:
            return 0;
        else:
            ldepth = self.chieucao(root.left)
            rdepth = self.chieucao(root.right)
            if ldepth >rdepth:
                return ldepth+1
            else:
                return rdepth+1


a=collections.deque()
while True:
    q = [int(x) for x in stdin.readline().split()]

    if q[0] == 3:
        b=Node()
        for i in a:
            b.addNode(i)
        print(b.chieucao(b))
        break
    elif q[0] == 2:
        if q[1] in a:
            a.insert(a.index(q[1])+1,q[2])
        else:
            a.insert(0,q[2])
    elif q[0] == 1:
        a.append(q[1])
    elif q[0] == 0:
        a.insert(0,q[1])
