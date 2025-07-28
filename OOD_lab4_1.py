class Queue :
    def __init__(self ,list= None):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        # enqueue method to add an item to the queue
    def dequeue(self):
        return self.items.pop(0) if self.items else None
        # dequeue method to remove the front item from the queue
    
    def isEmpty(self):
        return self.items == []
        # is_empty method to check if the queue is empty
    def size(self):
        return len(self.items)
        # size method to return the number of items in the queue
    def showitems(self):
        return self.items
        # show_items method to return the items in the queue

d = Queue()
value = input("Enter Input : ")
values = value.split(",")
n = 0
for i in values:
    item = i.split(" ")

    if item[0] == "E":
        d.enqueue(item[1])
        print(f"Add {item[1]} index is {d.size()-1}")

    elif item[0] == "D":
        if not d.isEmpty():
            N = d.dequeue()
            print(f"Pop {N} size in queue is {d.size()}")
        elif d.isEmpty():
            print("-1")

if not d.isEmpty():
    print(f"Number in Queue is :  {d.showitems()}")    
else:
    print("Empty")
    