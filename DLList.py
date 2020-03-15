class Node:
    def __init__(self, x):
        self.next = None
        self.prev = None
        self.x = x


class Dllist:

    def __init__(self):
        self.n = 0
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def add_before(self, w, x):
        u = Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def remove_Node(self, w):
        #print("remove1")
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def get_node(self, i):
        if i < (self.n / 2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
            #print(i)
        return p

    def get(self, i):
        return self.get_node(i).x

    def set(self, i, x):
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add(self, i, x):
        self.add_before(self.get_node(i), x)

    def print(self):
        l= self.dummy.next
        while l != self.dummy:
            print(l.x, end=" > ")
            l = l.next
        print(l.x)

    def remove(self, i):
        self.remove_Node(self.get_node(i))

    def push(self, x):
        self.add(0, x)

    def pop(self):
        self.remove(0)

x=Dllist()
x.add(0,"yes")
x.add(0,"yesafter")
x.print()
x.remove(0)
x.print()
x.set(0,"no")
x.print()
x.add(0,1)
x.add(0,2)
x.print()
x.add_before("1",no)
x.print()
