class Queue:
    def __init__(self):
        self.list = []
    
    def enqueue(self,data):
        self.list.append(data)

    def dequeue(self):
        if not self.list:
            return
        return self.list.pop(0)
        
    def front(self): #ใช้ดูตัวแรกของ Queue
        return self.list[0]

    def size(self):
        return len(self.list)
    
    def isEmpty(self):
        return len(self.list)==0 
    
    def __str__(self):
        return str(self.list)
    
class Stack():
    def __init__(self):
        self.items = []
        

    def isEmpty(self):
        return len(self.items)==0 
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class command():
    def __init__(self):
        self.cmd = None
        self.time = None
        self.data = None

inp = input('Enter input: ').split(', ')

q_print = Queue()
tray = Stack()
q_input = Queue()

for s in inp:
    #print(s)
    parts = s.split(" ", 1)
    cmd_time = parts[0]
    data = parts[1] if len(parts) > 1 else ""
    cmd, time = cmd_time.split(":")
    time = int(time)
    now_input = command()
    now_input.cmd = cmd
    now_input.time = time
    now_input.data =  data
    q_input.enqueue(now_input)

now_time = 0
paper = 3
now_order = next_print = None
now_paper = ""
while (not q_input.isEmpty()) or (now_order):
    if now_order:
        if paper != 0:
            now_paper = now_paper+ next_print[:5]
            next_print = next_print[5:]
            if next_print == "":
                paper=paper-1
                tray.push(now_order)
                #q_print.dequeue()
                #print(f"-->[Time {now_time}] now Print = {now_order}")
                now_order = next_print = None
                now_paper = ""
        else :
            print(f"[Time {now_time}] Error: Printer is out of paper. Please refill.")
    
    if (not q_print.isEmpty()) and (now_order == None):
        #print(f"-->[Time {now_time}] next print = {next_print}")
        if paper == 0:
            print(f"[Time {now_time}] Error: Printer is out of paper. Please refill.")
        else:
            now_order = next_print = q_print.dequeue()
    
   
    while (not q_input.isEmpty()) and (q_input.front().time == now_time):
        cmd = q_input.front().cmd
        data = q_input.front().data
        #data = 'xxx'
        q_input.dequeue()
        if cmd == 'P':
            if q_print.size() < 3 :
                q_print.enqueue(data)
                #print(f"[Time {now_time}] nowData={data}")
                if (not q_print.isEmpty()) and (now_order == None) and paper!=0:
                    now_order = next_print = q_print.dequeue()
                   #print(f"-->[Time {now_time}] next print = {next_print}")
                if paper == 0:
                    print(f"[Time {now_time}] Error: Printer is out of paper. Please refill.")
            else :
                print(f"[Time {now_time}] Error: Printer buffer is full. Please try again later.")
        elif cmd == 'S':
            if now_order:
                print(f'[Time {now_time}] Status: Printing... "{now_order}" and Pending {q_print.size()} file(s) in queue.')
            else:
                print(f'[Time {now_time}] Status: Idle. Pending {q_print.size()} file(s) in queue.')
        elif cmd == 'R':
            paper = paper+int(data)
            if (not q_print.isEmpty()) and (now_order == None) and paper!=0:
                    now_order = next_print = q_print.dequeue()
        elif cmd == 'T':
            if tray.isEmpty():
                print(f"[Time {now_time}] You got: Nothing in tray.")
                continue
            print(f"[Time {now_time}] You got: ",end="")
            while not tray.isEmpty():
                print(f'"{tray.pop()}"',end="")
                if not tray.isEmpty():
                    print(', ',end="")
            print()

    #print(q_print)  
    # if not q_print.isEmpty() and next_print == None:
    #     now_order = next_print = q_print.dequeue()
    #     if paper == 0:
    #         print(f"[Time {now_time}] Error: Printer is out of paper. Please refill.")
    # #print(q_print)
    #print(f"[Time {now_time}] nowpaper={now_paper} noworder={now_order}")
    now_time +=1
    #print('-----------------------------')