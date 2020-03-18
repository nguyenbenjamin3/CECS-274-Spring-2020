class Node:
    def __init__(self, x):
        self.parent = None
        self.left = None
        self.right = None
        self.x = x


class BinarySearchTree:
    def __init__(self):
        self.r = None
        self.n = 0

    def depth(self, u):
        found = False
        cNode = self.r
        depth = 0
        while not found:
            if u == cNode.x:
                return depth
            elif u > cNode.x:
                cNode = cNode.right
                depth += 1
            else:
                cNode = cNode.left
                depth += 1
        # d = 0
        # while u != self.r:
        #   u = u.parent
        #  d += 1
        # return d

    def size(self, u):
        if u is None:
            return 0
        return 1 + self.size(u.left) + self.size(u.right)

    def height(self, u):
        if u is None:
            return 0
        return 1 + max(self.height(u.left), self.height(u.right))

    def traverse(self, u):
        if u is None:
            return
        self.traverse(u.left)
        self.traverse(u.right)
        print(u.x)

    def traverse2(self):
        n = 0
        u = self.r
        prv = None
        while u is not None:
            if prv == u.parent:
                n += 1
                if u.left is not None:
                    nxt = u.left
                elif u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right is not None:
                    nxt = u.right
                else:
                    nxt = u.parent
            prv = u
            u = nxt
        print(self)

    def find_eq(self, x):  # returns the smallest value
        w = self.r
        while w is not None:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        return None

    def find(self, x):
        w = self.r
        z = None
        while w is not None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z is None:
            return None
        return z.x

    def add(self, x):
        p = self.find_last(x)
        # print(x)
        return self.add_child(p, Node(x))

    # def insert(self, x):
    #   if self.r is None:
    #      self.r = Node(x)
    # else:
    #    self.
    def find_last(self, x):
        w = self.r
        prev = None
        while w is not None:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def add_child(self, p, u):
        if p is None:
            self.r = u  # insert into empty tree
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False  # because u.x is already in tree
            u.parent = p
        self.n += 1
        return True

    def splice(self, u):
        if u.left is not None:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s is not None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u):
        if (u.left is None) | (u.right is None):
            self.splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.x = w.x
            self.splice(w)

    def traverse_inorder(self, r):
        if r:
            self.traverse_inorder(r.left)
            print(r.x)
            self.traverse_inorder(r.right)
        # return res

b = BinarySearchTree()
print(b.add(7))
print(b.add(5))
print(b.add(3))
print(b.add(8))
print(b.add(9))
print(b.add(1))
print(b.add(4))
print(b.add(9))
print(b.add(2))
print(b.add(6))
b.traverse_inorder(b.r)
print(b.height(b.r))
print(b.depth(9))
print(b.depth(5))
print(b.depth(4))
b.remove_node(b.r)
print(b.depth(4))
print(b.height(b.r))
