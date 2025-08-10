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
        self.item = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
            self.item += 1
        else:
            t = self.head
            while t.next != None:
                t=t.next
            t.next = p
            self.item += 1



    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p
        self.item += 1

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

    def size(self):
        if self.head == None:
            return 0
        return self.item

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        
        # ตำแหน่งติดลบ หรือเกินขนาดลิสต์
        if pos < 0 or pos >= self.item:
            return "Out of Range"
        t = self.head
        idx = 0
        if pos == 0:
            self.head = self.head.next
            self.item -= 1
            return "Success"
        while t.next is not None:
            if idx + 1 == pos :
                t.next = t.next.next
                self.item -= 1
                return "Success"
            t = t.next
            idx += 1

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        if len(i) < 4:
            print("Invalid")
            continue
        L.append(i[3:])
    elif i[:2] == "AH":
        if len(i) < 4:
            print("Invalid")
            continue
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
