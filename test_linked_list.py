class Node:
    def __init__(self, data ,next=None):
        self.data = data

        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)
    
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0