class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.item = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node
        self.item += 1
    def new_order(self, number):
        prev = None
        current = self.head
        first_group = True 
        if number <= 0 : return
        while current:
            head = None
            group_prev = prev
            for i in range(number):
                if not current: break
                if i == 0:
                    head = current
                    nxt = current.next
                    current.next = prev
                    prev = current
                    current = nxt
                else:
                    nxt = current.next
                    current.next = prev
                    prev = current
                    current = nxt
               
            if first_group:
                self.head = prev  
                first_group = False
            else:
                group_prev.next = prev 

            head.next = current
            for i in range(number):
                if not current: break
                prev = current
                current = current.next
                
        


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" → " if cur.next else "\n")
            cur = cur.next
    
print(" *** Ant Army ***")
list = LinkedList()
inp =  input("Input : ")
value = inp.split(",")
ant = value[0].split()
num = int(value[1])
for i in ant:
    list.append(i)
print("Before :", end=" ")
list.print_list()

list.new_order(num)

print("After :", end=" ")
list.print_list()