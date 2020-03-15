import sys
import re


def init():
    global n
    global a
    a = new_array(1)
    n = 0


def new_array(m):
    temp = []
    for i in range(m):
        temp.append(0)
    return temp


def add(i, x):
    global n
    if n == len(a):  # checks if number of elements is greater than array size
        resize()
    for j in range(i + 1, n):  # shifting positions to right
        a[j] = a[j + 1]
    a[i] = x  # add element to position i
    n += 1  # increasing total number of elements


def remove(i):
    global n
    x = a[i]
    for j in range(i, n - 2):
        a[j] = a[j + 1]
    if len(a) >= (3 * n):
        resize()
    n -= 1

    return x


def resize():
    global a
    b = new_array(max(1, 2 * n))
    for j in range(0, n):
        b[j] = a[j]
    a = b


def push(x):
    add(n, x)


def pop():
    return remove(n - 1)


def isEmpty():
    return n == 0


if len(sys.argv) < 2:  # checking that the number of parameters are correct
    print("wrong number of parameters")
    print("count filename k")
    exit

init()
with open(sys.argv[1], 'r') as f:  # Open the file
    for line in f:  # Read a line
        line = re.sub('[!#?,.:";\']', '', line).lower()  # removing punctuation marks
        token = line.split()  # Getting the tokens
        push(token)

while not isEmpty():
    print(pop())
