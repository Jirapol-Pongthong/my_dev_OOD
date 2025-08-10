n = 0     
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
        result = ""
        current_plates = []  


        for n in range(len(self.items)):
            item = self.items[n]
            plates = calculate_plates(item)
            if plates is None or (sum(plates) * 2 + 20 != item) or len(plates) > 5:
                display_weight = int(item) if item == int(item) else item
                result += f"It's impossible to achieve the weight you want({display_weight}).\n"
                break
            
            if item == 20 and not current_plates:  # กรณีพิเศษ ไม่ต้องใส่แผ่น
                result += "-----|======|----- => 20 KG.\n"
                current_plates = []
                continue
            
            diff, diffpu = calculate_plate_diff(current_plates, plates)
            if plates != current_plates:  # ถ้าเปลี่ยนแผ่น
                if diff:
                    result += "PO:" + " PO:".join(str(p) for p in diff) + " "

                if diffpu:
                    result += "PU:" + " PU:".join(str(p) for p in diffpu) + " "

                result += "=> "
            dashes = get_dashes(len(plates))
            left = ''.join(f"[{p}]" for p in plates[::-1])
            right = ''.join(f"[{p}]" for p in plates)
            
            display_weight = int(item) if item == int(item) else item
            for i in diffpu:
                if isinstance(i, float):
                    display_weight = item
                    break
            
            result += f"{dashes}{left}|======|{right}{dashes} => {display_weight} KG.\n"
            current_plates = plates 


        return result
    
def get_dashes(num_plates):

    count = max(0, 5 - num_plates)
    return "-" * count

def calculate_plates(target_weight, bar_weight=20):
    plates = [25, 20, 15, 10, 5, 2.5, 1.25]
    target_per_side = (target_weight - bar_weight) / 2

    if target_per_side < 0:
        return []

    used_plates = []
    remaining = target_per_side

    for plate in plates:
        while remaining >= plate:
            used_plates.append(plate)
            remaining -= plate

    return used_plates
def calculate_plate_diff(current_plates, next_plates):
    po = []
    pu = []
    stack = current_plates[:]

    # ถอดทีละแผ่นจากนอกสุดไปในสุด
    while stack and stack != next_plates[:len(stack)]:
        po.append(stack.pop())

    # ใส่กลับถ้าต้องใช้อีก
    remaining = next_plates[len(stack):]
    for p in remaining:
        pu.append(p)

    return po, pu

value = input("Enter needed weight(s): ")
s = Stack()
values = value.split()
for i in values:
    num = float(i)

    s.push(num)
    n += 1

print(s)