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

    def peek_next(self,i):
        return self.items[i+1] if len(self.items) > 1 else None
    def is_empty(self):
        return self.items == []
        # is_empty method to check if the stack is empty
    def __str__(self):
        s = "Output : "
        for item in self.items:
            s += str(item) + " "
        return s
    
s = Stack()
print("*****Big leg on the right side*****")
value = input("Enter input: ")
values = value.split()
number_of_index = len(values)
ans = [-1]*number_of_index


for i in range(number_of_index):
    try:
        while not s.is_empty() and values[i] > values[s.peek()]:
            index = s.pop()
            print(f"input[{i}]({values[i]}) is greater than input[top of stack]({values[index]})")
            ans[index] = int(values[i])
            print(f"Stack pop")
            print(f"Output: {ans}")
        s.push(i)
        print(f"Stack push {i} index of {values[s.peek()]}")
    except ValueError:
        print(f"'{i}' is Invalid Input !!!")
        break
print(f"Output: {ans}")

