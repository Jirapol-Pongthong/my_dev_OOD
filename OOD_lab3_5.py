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

    def check(self, item):
        if item in self.items:
            return True
        return False
        # check method to see if an item is in the stack

    def pop_specific(self, item):
        if item in self.items:
            self.items.remove(item)
            self.size -= 1
            return item
        else:
            return None
        # pop_specific method to remove a specific item from the stack
    def number_of_item(self):
        return len(self.items)
        # method to return the number of items in the stack

    def is_empty(self):
        return self.items == []
        # is_empty method to check if the stack is empty
    def __str__(self):
        a = ""
        for i in self.items:
            a += str(i) + ", "
        a = a[:-2]
         # Remove the trailing comma
        return a
    
s = Stack()
print("******** Parking Lot ********")
value = input("Enter max of car,car in soi,operation : ")
values = value.split()
car = values[1].split(",")
car = [int(c) for c in car]
for i in car:
    if i != 0:
        s.push(i)

if values[2] == "arrive" and int(values[0]) > s.number_of_item():
    if not s.check(int(values[3])):
        print(f"car {values[3]} arrive! : Add Car {values[3]}")
        s.push(int(values[3]))
        print(f"[{s}]")
    else:
        print(f"car {values[3]} already in soi")
        print(f"[{s}]")
elif values[2] == "arrive" and int(values[0]) <= s.number_of_item():
    print(f"car {values[3]} cannot arrive : Soi Full")
    print(f"[{s}]")

if values[2] == "depart" and s.is_empty():
    print(f"car {values[3]} cannot depart : Soi Empty")
    print(f"[{s}]")

elif values[2] == "depart" and not s.is_empty():
    if s.pop_specific(int(values[3])) is not None:
        print(f"car {values[3]} depart ! : Car {values[3]} was remove")
        print(f"[{s}]")
    else:
        print(f"car {values[3]} cannot depart : Dont Have Car {values[3]}")
        print(f"[{s}]")