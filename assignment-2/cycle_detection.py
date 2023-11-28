import argparse
import sys
from collections import defaultdict
import math

parser = argparse.ArgumentParser(description="fml")
parser.add_argument("tt", type=str, nargs="+")
parser.add_argument("-t", default=False, action="store_true")
args = parser.parse_args()

b = int(args.tt[0])
g = int(args.tt[1])
max_size = int(args.tt[2])

with open(sys.argv[-1], 'r') as f:
    x = int(f.readline())

def f(y):
    global x
    with open(sys.argv[-1], 'r') as f:
        while True:
            contents = f.readline()
            if len(contents) == 0:
                x = "fin"
                break
            if int(contents) == y:
                contents = f.readline()
                x = int(contents)
                break
    return x

def InsertInTable(table, y, i):
    data = []
    data.append(y)
    data.append(i)
    table.append(data)
    return

def SearchTableY(table, y):
    pos = -1
    for i in range (len(table)):
        if table [i][0] == y :
            pos = table[i][1]
    return pos

def SearchTableJ(table, j):
    lb = -1
    for i in range (len(table)):
        if table [i][1] == j :
            lb = table[i][0]
    return lb

def Purge(table, b):
    topop = []
    for i in range (len(table)):
        if table [i][1] % (2 * b) != 0 :
            topop.append(i)
    for i in range (len(topop)):
        pos = topop[i]
        table.pop(pos)
        for j in range (len(topop)):
            topop[j] = topop[j] - 1
    return table

def detect (x):
    global b, y, i , j, table
    y = x 
    i = 0
    m = 0
    table = []
    while True:
        if i % b == 0 and m == max_size:
            b = 2 * b
            Purge (table, b)
            m = m / 2
        if i % b == 0:
            InsertInTable(table, y,i)
            m = m + 1
        y = f(y)
        i = i + 1
        if i % (g * b) < b:
            j = SearchTableY(table, y)
            if j != -1:
                return(y,i,j)
        if f(y) == "fin": 
            break

def recover(y ,i, j): 
    global c,l, table
    c = 1
    foundc = False
    yc = y
    while c <= (g + 1) * b and foundc == False:
        yc = f(yc) 
        if y == yc:
            foundc = True
        else:
            c = c + 1
    if foundc == False:
        c = i - j
    blocklen = g * b
    finblock = blocklen * ( i / blocklen)
    prev = finblock - blocklen
    ii = max(c, prev)
    jj = ii - c
    l = jj + 1
    jb = b * (l / b)
    jcb = b * ((l + c) / b)
    lb = SearchTableJ(table, jb)
    lcb = SearchTableJ(table, jcb)
    upto = l % b
    if (upto + 0.5) <= math.ceil(upto):
        upto = math.floor(upto)
    else:
        upto = math.ceil(upto)
    for i in range (upto): 
        fl = f(lb) 
        lb = fl
    upto = (l + c) % b
    if (upto + 0.5) <= math.ceil(upto):
        upto = math.floor(upto)
    else:
        upto = math.ceil(upto)
    for i in range (upto): 
        flc = f(lcb)
        lcb = flc
    while fl != flc:
        l = l + 1
    return c, int(l)

detect(x)
recover(y, i, j)
print("cycle " +str(c), "leader " +str(l))

if args.t:
    for i in range (len(table)):
        print(table[i][0], table[i][1])
