class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key
        def __repr__(self):
            return f"Node({self.val})"
class Queue :
    def __init__(self ,list= None):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    def check(self,data):
        if data in self.items:
            return True
        return False
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def showitems(self):
        return self.items

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)
        return self.root
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                return self._insert(node.left,key)
        if key >= node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                return self._insert(node.right,key)
    def convert_tree (self,number):
        self._convert_tree(self.root,number)
    def _convert_tree(self,node,number):
        if node is not None:
            if number < node.val:
                node.val = node.val*number
            self._convert_tree(node.right,number)
            self._convert_tree(node.left,number)
        

    def BFS(self):
        q = Queue()
        q.enqueue(self.root)
        result = []
        sum = 0
        while not q.isEmpty() :
            n = q.dequeue()
            result.append(n.val)
            if n.left is not None :
                q.enqueue(n.left)
            if n.right is not None :
                q.enqueue(n.right)
        for i in result:
            sum += i
        return sum
    def preOrder(self):
        result = []
        self._preOrder(self.root,result)
        return result
    def _preOrder(self,root,result):
        if root is not None:
            result.append(root.val)
            self._preOrder(root.right,result)
            self._preOrder(root.left,result)


    def __str__(self):
        return self._print_tree(self.root, 0)
    def _print_tree(self, node, level):
        if node is None:
            return ""
        result = self._print_tree(node.right, level + 1)
        result += "     " * level + f" {node.val}\n"
        result += self._print_tree(node.left, level + 1)
        return result


inp = input("Enter Input : ")
inp = inp.split()
T = BST()
for i in inp:
    T.insert(i)

print(T.preOrder())
print(T)