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

main = Queue()

print(" ***Queue of Queue of Queue of ...***")
value = input("Enter Input : ")
values = value.split(",")

for i in values:
    command = i.strip().split()
    if command[0] == "en":
        if main.isEmpty():
            sub_main = Queue()
            sub_main.enqueue(int(command[1]))
            main.enqueue(sub_main)
            print(f"Enqueued: {command[1]}")
            print(f"Queue state: {[q.showitems() for q in main.showitems()]}")
        else:
            found = False
            for j in main.showitems():
                for k in j.showitems():
                    if int(k) // 100 == int(command[1]) // 100:
                        j.enqueue(int(command[1]))
                        print(f"Enqueued: {command[1]}")
                        print(f"Queue state: {[q.showitems() for q in main.showitems()]}")
                        found = True
                        break
                if found:
                    break
            if not found:
                sub_main = Queue()
                sub_main.enqueue(int(command[1]))
                main.enqueue(sub_main)
                print(f"Enqueued: {command[1]}")
                print(f"Queue state: {[q.showitems() for q in main.showitems()]}")
    elif command[0] == "de":
        if not main.isEmpty():
            first_queue = main.seek_no_1()
            removed = first_queue.dequeue()
            print(f"Dequeued: {removed}")
            if first_queue.isEmpty():
                main.dequeue()
            print(f"Queue state: {[q.showitems() for q in main.showitems()]}")
        else:
            print("Queue is empty")
        




                
