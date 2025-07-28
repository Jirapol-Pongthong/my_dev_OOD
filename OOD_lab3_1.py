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
    def is_empty(self):
        return self.items == []
        # is_empty method to check if the stack is empty
    def __str__(self):
        s = "Output : "
        for item in self.items:
            s += str(item) + " "
        return s

s = Stack()
print("***Always 5 or 10***")
value = input("Enter Input : ")
values = value.split()
n = 0
for i in values:
    try:
        num = int(i)
    except ValueError:
        print(f"'{i}' is Invalid Input !!!")
        break
    if n == 0:
        s.push(num)
    elif  s.peek() + num == 5 or s.peek()+num == 10 or s.peek()-num == 5 or s.peek()-num == 10:
        s.push(num)
    n += 1

print(s)



