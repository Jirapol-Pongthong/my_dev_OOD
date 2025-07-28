class Stack:
 
    def __init__(self,list=None):
        if list is None:
            self.items = []
            self.first = True
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
    def dmg(self, value):
        count = 0
        ans = value
        while self.items and value > 0:
            top = self.items[-1]
            if isinstance(top, int):
                if top <= value:
                    value -= top
                    self.items.pop()
                    count += 1
                else:
                    self.items[-1] -= value
                    value = 0
            else:
                # ถ้าเป็น command string ก็ pop ทิ้ง
                self.items.pop()
        result = f"deal {ans} damage, killed {count} enemy\n{self.items}"
        if self.is_empty():
            result += "\n\n>>>> Player Wins <<<<"
        return result

    def __str__(self):
        if self.first:
            self.first = False
            return "start\n" + str(self.items)+"\n"

        top = self.items[-1]
        if isinstance(top, str):
            cmd = top.split()
            if cmd[0] == "spawn":
                s = f"spawn an enemy of {cmd[1]} HP\n"
                self.items[-1] = int(cmd[1])  
                return s + str(self.items)+"\n"
            elif cmd[0] == "dmg":
                dmg_val = int(cmd[1])
                self.items.pop() 
                if dmg_val > 0:
                    return self.dmg(dmg_val)+ "\n"
                else:
                    return "Invalid number"  
        # if self.is_empty():
        #     s = "[]\n"+">>>> Player Wins <<<<"
        #     return s
        return str(self.items)

    
s = Stack()
value = input("Enter Input : ")
values = value.split("/")
values[0] = values[0].split()
values[1] = values[1].split(",")
for i in values[0]:
    try:
        if int(i) > 0 :
            num = int(i)
            s.push(num)
        else:
            continue
    except ValueError:
        print(f"'{i}' is Invalid Input !!!")
        break

print()
print(s)
for i in values[1]:
    s.push(i)
    print(s)


# print(values[0])
# print(values[1])