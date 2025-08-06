rem_W = []
rem_A = []
fight_fail = 0
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
        self.power_w = 5
        self.power_a = 10
        self.carry_w = 2
        self.carry_a = 5

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
    
    def removing_at_head(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head  = None
        else:
            p = self.head
            self.head = self.head.next
        self.item -= 1
        return p.value


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
        return self.item

    def carry_food(self,number):
        round = 0
        while number > 0 and self.head :
            ant = self.head.value[0]
            if ant == "W":
                capacity = 2
            else:
                capacity = 5
            carry.append(self.head.value)
            self.head = self.head.next
            self.item -= 1
            round += 1
            number -= capacity
        if number > 0 and self.item == 0 :
            if not carry:
                carry.append("Empty")
            round = 0
            return False
        return True
    

    def Fight (self,number):
    
        while number > 0 and self.head:
            ant = self.head.value[0]
            if ant== "W":
                power = 5
            else:
                power = 10
            fight.append(self.head.value)
            self.head = self.head.next
            self.item -= 1
            number -= power
        if self.item == 0 and number > 0:
            return False
        return True

    def check_ant(self):
        rem_W.clear()
        rem_A.clear()
        t = self.head
        while t:
            if t.value[0] == "W":
                rem_W.append(t.value)
            else:
                rem_A.append(t.value)
            t = t.next


print("***This colony is our home***")
value = input("Enter input : ")
values = value.split("/")
num_of_ant = values[0]
num_of_ant = num_of_ant.split()
cmd = values[1]
cmd = cmd.split(",")
list = LinkedList()
for i in range(1,int(num_of_ant[0])+1):
    list.append(f"W{i}")
for i in range(1,int(num_of_ant[1])+1):
    list.append(f"A{i}")
print(f"Current Ant List: {list}\n")
queen_angry_count = 0
for i in cmd:
    word = i.split()
    if word[0] == "C":
        carry = []
        success = list.carry_food(int(word[1]))
        print(f"Food carrying mission : {' '.join(carry)}")
        if not success:
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
            queen_angry_count += 1
        if queen_angry_count >= 3:
            print("**The queen is furious! The ant colony has been destroyed**")
            break
    if word[0] == "F":
        fight = []
        success = list.Fight(int(word[1]))
        print(f"Attack mission : {' '.join(fight)}")
        if not success:
            print("Ant nest has fallen!")
            break
            
    if word[0] == "S" :
        rem_W.clear()
        rem_A.clear()
        list.check_ant()
        print(f"-> Remaining worker ants: {' '.join(rem_W) if rem_W else 'Empty'}")
        print(f"-> Remaining soldier ants: {' '.join(rem_A) if rem_A else 'Empty'}")

    if word[0] == "W":
        for i in range(1,int(word[1])+1):
            list.append(f"W{i}")
    if word[0] == "A":
        for i in range(1,int(word[1])+1):
            list.append(f"A{i}")
    







