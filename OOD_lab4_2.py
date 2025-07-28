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
        return self.items == []
        # is_empty method to check if the queue is empty
    def size(self):
        return len(self.items)
        # size method to return the number of items in the queue
    def showitems(self):
        return self.items
        # show_items method to return the items in the queue
q1 = Queue()
q2 = Queue()
q3 = Queue()
value = input("Enter people and time : ")
values = value.split()
time = int(values[1])
n = 0
a = 0
for i in values[0]:
    q1.enqueue(i)

for i in range(time+1):

 
    if i > 0 and q2.size() < 5 :
        move = q1.dequeue()
        q2.enqueue(move)
    if i > 0 and q2.size() > 4:
        if not q1.isEmpty():
            move_2 = q1.dequeue()
            q3.enqueue(move_2)
    if not q2.isEmpty():
        q2.dequeue()
    if not q3.isEmpty():
        q3.dequeue()
    if i > 0:
        print(f"{i} {q1.showitems()} {q2.showitems()} {q3.showitems()}")