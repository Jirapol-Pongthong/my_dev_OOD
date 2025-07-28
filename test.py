# class Stack:
 
#     def __init__(self,list=None):
#         if list is None:
#             self.items = []
#         else:
#             self.items = list
#         self.size = len(self.items)
#     def push(self, item):
#         self.items.append(item)
#         self.size += 1
#         # push method to add an item to the stack 
#     def pop(self):
#         return self.items.pop() if self.items else None
#         # pop method to remove the top item from the stack
#         # ต้อง return ค่าออกมาด้วยไม่งั้นเราไม่รู็ว่า pop แล้วได้ค่าอะไร
#     def peek(self):
#         return self.items[-1] if self.items else None
#         # peek method to view the top item without removing it
#     def is_empty(self):
#         return self.items == []
#         # is_empty method to check if the stack is empty
#     def __str__(self):
#         s = "Stack of : "+ str(self.size) + " items -> "
#         for item in self.items:
#             s += str(item) + "  "
#         return s
# s = Stack()
# s.push("A")
# s.push("B")
# s.push("C")
# print(s.items) 
# print(s.size)
# s.pop()
# print(s.items)
# print(s.peek())
# print(s.is_empty())

# print(s)
# a = [1, 2, 3]
# b = a[:]   # b เป็นสำเนาของ a
# b.remove(2)
# print(b) 
w = "0p"
if 0 in w  :
    print("a")