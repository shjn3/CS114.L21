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


    def dem(self):
        if self.data is not None:
            if self.left is None and self.right is None:
                return 1
            if self.left is not None and self.right is not None:
                return self.left.dem() + self.right.dem()
            if self.left is None:
                return self.right.dem()
            if self.right is None:
                return self.left.dem()
        else:
            return 0
a = Node()
while True:
    q = int(input())
    if q == 0:
        print(a.dem())
        break
    a.addNode(q)
