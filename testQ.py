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
        first_group = True  # ใช้เช็คกลุ่มแรก

        while current:
            head = None
            group_prev = prev  # node ก่อนกลุ่มนี้
            group_start = current  # node แรกของกลุ่มนี้

            # reverse number ตัวแรกของกลุ่มนี้
            for i in range(number):
                if current:
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
                else:
                    break

            # ตอน reverse เสร็จ กลุ่มนี้จะเริ่มที่ prev (หัวใหม่)
            if first_group:
                self.head = prev  # อัปเดต head ครั้งแรก
                first_group = False
            else:
                group_prev.next = prev  # ต่อจากกลุ่มก่อนหน้า

            # หางของกลุ่มนี้ (head) ต้องต่อกับ node ถัดไป (current)
            head.next = current

            # ข้ามกลุ่มถัดไป (ไม่ reverse)
            for i in range(number):
                if current:
                    prev = current
                    current = current.next
                else:
                    break


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
list.new_order(num)
list.print_list()