class Node:
        def __init__(self, value,next = None):
            self.value = value
            if next == None:
                self.next = None
            else:
                self.next = next


class LinkedList:
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def append(self,data):
        p = Node(data)
        if self.head == None :
            self.head = p
            self.size += 1
        else:

            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
            self.tail = p
            self.size += 1


    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item :
                return "Found"
            t=t.next
        return "Not Found"
    
    def index(self, item):
        t = self.head
        idx = 0
        while t is not None:
            if t.value == item:
                return idx
            t = t.next
            idx += 1
        return -1
    
    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.value))
            node = node.next
        return '->'.join(ans)
    
    def sort(self):
        n = self.size
        if not self.head or not self.head.next:
            return "Invalid"

        end = None  
        while True:
            swapped = False
            cur = self.head

            while cur.next != end:  
                
                if cur.value > cur.next.value:
                    cur.value, cur.next.value = cur.next.value, cur.value
                    swapped = True
                    print(f"\nSwapping {cur.next.value} and {cur.value}")
                    print(f"List: {self}")
                cur = cur.next
            end = cur 
            if not swapped:
                break

print("*****Bubble Sort Linked List*****")
value = input("Enter Input: ")
values = value.split(",")
L = LinkedList()
for i in values:
    L.append(int(i))
print(f"Input List: {L}")
print("_______________________________________")
L.sort()
print("_______________________________________")
print(f"Sorted List: {L}")
# print(L)