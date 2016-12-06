class Node(object):

    # constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #takes in a node value and looks to the left and right node to see where to insert
    def insert(self, value):
        if (value <= self.data):
            if(self.left is None):
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if(self.right is None):
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if(value == self.data):
            return True
        elif(value < self.data):
            if(self.left is None):
                return False
            else:
                return self.left.contains(value)
        else:
            if(self.right is None):
                return False
            else:
                return self.right.contains(value)

    #Tree Traversal
    #   B       Inorder:    Left, Root, Right (A -> B -> C) ** Typical **
    #  / \      Preorder:   root, left, right (B -> A -> C)
    # A   C     Postorder:  left, right, root (A -> C -> B)
    def printTree(self):
        self.__inorder()

    def __inorder(self):
        if(not(self.left is None)):
            self.left.__inorder();

        print(self.data)

        if(not(self.right is None)):
            self.right.__inorder();

    def __preorder():
        print(self.data)

        if(not(self.left is None)):
            self.left.__inorder();

        if(not(self.right is None)):
            self.right.__inorder();

    def __preorder():
        if(not(self.left is None)):
            self.left.__inorder();

        if(not(self.right is None)):
            self.right.__inorder();

        print(self.data)
