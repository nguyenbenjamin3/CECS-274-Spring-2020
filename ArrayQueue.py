from _ctypes import resize
import sys
import re


def new_array(m):
    temp = []
    for i in range(m):
        temp.append(0)
    return temp


class Queue:

    def __init__(self):
        self.a = new_array(1)  # name of queue
        self.j = 0  # Head of circle queue
        self.n = 0  # number of elements in queue

    def add(self,x):
        if (self.n + 1) > len(self.a):
            self.resize()
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n += 1
        return True

    def remove(self):
        x = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        if len(self.a) >= (3 * self.n):
            self.resize()
        return x

    def resize(self):
        b = new_array(max(1, 2 * self.n))
        for k in range(0, self.n - 1):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0

    def isEmpty(self):
        return self.n == 0


if len(sys.argv) < 2:  # checking that the number of parameters are correct
    print("wrong number of parameters")
    print("count filename k")


with open(sys.argv[1], 'r') as f:  # Open the file
    mobyd = Queue()
    for line in f:
        line = re.sub('[!#?,.:";\']', '', line).lower()  # removing punctuation marks
        token = line.split()  # Getting the tokens
        mobyd.add(token)
        while not mobyd.isEmpty():
            print('-', mobyd.remove())
