class Queue :
    def __init__(self ,list= None):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        # enqueue method to add an item to the queue
    def dequeue(self):
        return self.items.pop(0) if self.items else None
        # dequeue method to remove the front item from the queue
    def seek_no_1(self):
        return self.items[0] if self.items else None
        # seek_no_1 method to return the front item without removing it
    def isEmpty(self):
        if self.items == [] :
            return True
        else :
            return False
        # is_empty method to check if the queue is empty
    def size(self):
        return len(self.items)
        # size method to return the number of items in the queue
    def showitems(self):
        return self.items
        # show_items method to return the items in the queue
    def __str__(self):
        return str(self.items)

class Stack:
 
    def __init__(self,list=None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)
    def push(self, item):
        self.items.append(item)
        self.size += 1
        # push method to add an item to the stack 
    def pop(self):
        return self.items.pop() if self.items else None
        # pop method to remove the top item from the stack
        # ต้อง return ค่าออกมาด้วยไม่งั้นเราไม่รู็ว่า pop แล้วได้ค่าอะไร
    def peek(self):
        return self.items[-1] if self.items else None
        # peek method to view the top item without removing it

    def peek_next(self,i):
        return self.items[i+1] if len(self.items) > 1 else None
    def is_empty(self):
        return self.items == []
        # is_empty method to check if the stack is empty

q = Queue()
stack = Stack()
value = input("Enter input: ")
values = value.split(",")
for i in values:
    cmd = i.split()
    
