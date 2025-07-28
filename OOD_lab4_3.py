class Queue :
    def __init__(self ,list= None):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        # enqueue method to add an item to the queue
    def dequeue(self):
        return self.items.pop(0) if self.items else None
        # dequeue method to remove the front item from the queue
    def seek_no_1(self):
        return self.items[0] if self.items else None
        # seek_no_1 method to return the front item without removing it
    def isEmpty(self):
        return self.items == []
        # is_empty method to check if the queue is empty
    def size(self):
        return len(self.items)
        # size method to return the number of items in the queue
    def showitems(self):
        return self.items
        # show_items method to return the items in the queue
def encodemsg(q1, q2):
    for i in q1.showitems():
        q2.enqueue(q2.seek_no_1())
        if ord(i) + int(q2.seek_no_1()) > 64 and ord(i) + int(q2.seek_no_1()) < 91 or ord(i) + int(q2.seek_no_1()) > 96 and ord(i) + int(q2.seek_no_1()) < 123:
            en = ord(i) + int(q2.dequeue())
            encode.append(chr(en))
        elif ord(i) + int(q2.seek_no_1()) > 90 and ord(i) + int(q2.seek_no_1()) < 97:
            en = ord(i) + int(q2.dequeue()) - 26
            encode.append(chr(en))
        elif ord(i) + int(q2.seek_no_1()) > 122:
            en = ord(i) + int(q2.dequeue()) - 26
            encode.append(chr(en))

    print(f"Encode message is :  {encode}")
def decodemsg(q1, q2):
    for i in encode:
        q2.enqueue(q2.seek_no_1())
        if ord(i) - int(q2.seek_no_1()) > 64 and ord(i) - int(q2.seek_no_1()) < 91 and ord(i) >= 65 and ord(i) <= 90:
            en = ord(i) - int(q2.dequeue())
            decode.append(chr(en))
        elif ord(i) - int(q2.seek_no_1()) > 96 and ord(i) - int(q2.seek_no_1()) < 123 and ord(i) >=97 and ord(i) <= 122:
            en = ord(i) - int(q2.dequeue())
            decode.append(chr(en))
        elif ord(i) - int(q2.seek_no_1()) < 90 and ord(i) - int(q2.seek_no_1()) > 97 :
            en = ord(i) - int(q2.dequeue()) + 26
            decode.append(chr(en))
        elif ord(i) - int(q2.seek_no_1()) < 122:
            en = ord(i) - int(q2.dequeue()) + 26
            decode.append(chr(en))
    print(f"Decode message is :  {decode}")

q1 = Queue()

q2 = Queue()

value = input("Enter String and Code : ")
values = value.split(",")
values[0] = values[0].split()
num = []
word = []
encode= []
decode = []
temp = Queue()
for i in values[0]:
    n = list(i)
    for j in n:
        q1.enqueue(j)
        word.append(j)
for i in values[1]:
    if i.isdigit():
        num.append(int(i))
        q2.enqueue(int(i))
        temp.enqueue(int(i))

encodemsg(q1, q2)
decodemsg(q1, temp)