class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, v):
        n = Node(v)
        if not self.head:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    def get_root(self):
        n = self.head
        while n and n.next:
            n = n.next
        return n.val if n else None

class BranchNode:
    def __init__(self, branch):
        self.branch = branch
        self.next = None

def find_commit_info(head, val):
    n = head
    while n:
        if n.val == val:
            return n
        n = n.next
    return None

def all_same(head):
    if not head:
        return True
    v = head.val
    n = head.next
    while n:
        if n.val != v:
            return False
        n = n.next
    return True

def collect_commits(branch_head):
    head = None
    b = branch_head
    while b:
        n = b.branch.head
        while n:
            ci = find_commit_info(head, n.val)
            if not ci:
                ci = Node(n.val)
                ci.next = head
                head = ci
                ci.locations = None
            loc = Node((b, n))
            loc.next = ci.locations
            ci.locations = loc
            n = n.next
        b = b.next
    return head

def count_merges(branch_head):
    if not branch_head:
        return 0
    root = branch_head.branch.get_root()
    ci = collect_commits(branch_head)
    merges = 0
    while ci:
        if ci.val != root:
            # นับ branch ที่มี commit นี้
            cnt = 0
            loc = ci.locations
            nexts = None
            while loc:
                cnt += 1
                nxt_val = loc.val[1].next.val if loc.val[1].next else None
                n = Node(nxt_val, nexts)
                nexts = n
                loc = loc.next
            if cnt > 1 and not all_same(nexts):
                merges += 1
        ci = ci.next
    return merges

def check_same_repo(branch_head):
    if not branch_head:
        return True
    root = branch_head.branch.get_root()
    b = branch_head
    while b:
        if b.branch.get_root() != root:
            return False
        b = b.next
    return True

# อ่าน input
inp = input("Git History: ")
branches = inp.split("|")
branch_head = None
last = None
for br in branches:
    br = br.strip()
    commits = [c.strip() for c in br.split("->")]
    ll = LinkedList()
    for c in commits:
        ll.append(c)
    bn = BranchNode(ll)
    if not branch_head:
        branch_head = bn
    else:
        last.next = bn
    last = bn

same_repo = check_same_repo(branch_head)
print(f"Are these branches in the same repository? {same_repo}")
if same_repo:
    print(f"{count_merges(branch_head)} Merge(s)")
