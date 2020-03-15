#DOES NOT FULLY WORK
import DLList


class HashTable:

    def __init__(self):
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 10101001011
        self.n = 0
        self.w = 2

    def add(self, x):
        if self.find(x) != None:
            return False
        if self.n + 1 > len(self.t):
            self.resize()
        self.t[self.hash(x)].push(x)
        self.n += 1
        return True

    def remove(self, x):
        y = self.t[self.hash(x)].dummy.next
        while y != self.t[self.hash(x)].dummy:
            if y.x == x:
                self.t[self.hash(x)].remove(x)
                self.n += 1
                if (3 * self.n) < len(self.t):
                    self.resize()
                    return y
                return None
            y = y.next

    def find(self, x):
        y = self.t[self.hash(x)].dummy.next
        while y != self.t[self.hash(x)].dummy:
            if y.x == x:
                return y
            y = y.next
        return None

    def resize(self): #Does not work
        self.d += 1
        temp.table = self.alloc_table(2 ** self.d)
        for i in [0, 2 ** (self.d - 1)]:
            temp.table[i] = self.t[i]
        self.t = self.alloc_table(2 ** self.d)
        for i in [0, 2 ** (self.d - 1)]:
            if temp[i] != None:
                for i in self.t:
                    self.add(temp[i])

    def hash(self, x):
        return ((self.z * x) % 2 ** self.w) >> (self.w - self.d)

    def alloc_table(self, m):
        stack = []
        for i in range(m):
            stack.append(DLList.Dllist())
        return stack


d = HashTable()
print(d.add(9))
print(d.add(4))

print(d.find(9).x)
print(d.find(4).x)
print(d.remove(9))
print(d.remove(4))

print(d.find(9))
print(d.find(4))

print(d.add(21))
print(d.find(21).x)