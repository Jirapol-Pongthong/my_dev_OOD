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


inp = input("Git History: ")
branch_strings = inp.split("|")
branch_head = None
last_branch = None

for branch_str in branch_strings:
    branch_str = branch_str.strip()
    commits = [c.strip() for c in branch_str.split("->") if c.strip()]  # ใช้ list แค่ตรงนี้
    commit_ll = LinkedList()

    for commit_id in commits:
        commit_ll.append(commit_id)

    # สร้าง node ของ branch
    branch_node = Node(commit_ll)
    if branch_head is None:
        branch_head = branch_node
    else:
        last_branch.next = branch_node
    last_branch = branch_node


b = branch_head
count = 1
while b:
    print(f"Branch {count}: {b.branch}")
    b = b.next
    count += 1


