import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('t', type=str)
parser.add_argument('f', type=str)
parser.add_argument('l', type=str)
parser.add_argument('g', type=int)
parser.add_argument('m', type=int)
parser.add_argument('d', type=int)
parser.add_argument('A', type=str)
parser.add_argument('B', type=str)
args = parser.parse_args()
#print('data:', args.x, args.y, args.z)

#def enumerate_allignments():

a = sys.argv[len(sys.argv) - 2]

b = sys.argv[len(sys.argv) - 1]
g = args.g
m = args.m
d = args.d
#print(a)
#print(b)
ww = []
zz = []

def enumerate_allignments(A, B, w, z):
    i = len(A)
    j = len(B)
    print("i " + str(i))
    print("j " + str(j))
    ff = []
    f =[]
    #na ftiajw ton F
    for y in range(len(B) + 1):
        if y!= 0 :
            ff.append(y * g)
        elif y ==0:
            ff.append(0)
    f.append(ff)
    for x in range( 1, len(A) + 1):
        ff = []
        for y in range(len(B) + 1):
            if y == 0:
                ff.append(x * g)
            else:
                if A[x - 1] == B[y - 1]:
                    res = f[x-1][y-1] + m
                else :
                    res = f[x-1][y-1] + d
                g1 = ff[y-1] + g
                g2 = f[x-1][y] + g
                fin = max(g1, g2 , res)
                ff.append(fin)
        f.append(ff)
    #telosF
    #print("F" + str(f))
    if i == 0 and j == 0:
        ww.append(w)
        zz.append(z)
        return ww, zz
    if i > 0 and j > 0 :
        if A[i - 1] != B[j - 1] :
            md = d
        else :
            md = m
        if f[i][j] == f[i - 1][ j - 1] + md :
            enumerate_allignments(A[:i - 1], B[:j - 1], A[i-1] + w, B[j-1] + z) 
    if i > 0 and (f[i][j] == (f[i-1][j] + g)):
        #print("mpainw")
        enumerate_allignments(A[:i - 1], B, A[i-1] + w, "-" + z)
    if j > 0 and (f[i][j] == (f[i][j -1] + g)):
        #print("bhka")
        enumerate_allignments(A, B[:j - 1], "-" + w, B[j-1] + z)
    #print(ww, zz)

#print(enumerate_allignments(sys.argv[7],sys.argv[8], "",""))
enumerate_allignments(sys.argv[7],sys.argv[8], "","")

def compute_allignments(A, B):
    l = []
    for j in range(len(B) + 1):
        l.append(j * g)
    k = []
    for i in range(1, len(A) + 1):
        temp = l
        l = k
        k = temp
        l = []
        l.insert(0, i * g)
        for j in range(1, len(B) + 1):
            if A[i - 1] != B[j - 1] :
                md = d
            else :
                md = m
            res = max(l[j-1] + g, k[j] + g, k[j - 1] + md)
            l.append(res)
    return l

#print(compute_allignments(sys.argv[7], sys.argv[8]))

def hirschberg(A, B):
    if len(A) == 0:
        ww = "-" * len(B)
        zz = B
    elif len(B) == 0:
        ww = A
        zz = "-" * len(A)
    elif len(A) == 1 or len(B) == 1:
        ww , zz = enumerate_allignments(A, B, "" , "")
    else:
        i = len(A) // 2
        al = A[:i]
        sl = compute_allignments(al, B)
        #antistrofh string me [::-1]
        ar = A[i:]
        sr = compute_allignments(ar[::-1], B[::-1])
        srtonos = sr[::-1]
        s = []
        for fml in range(len(B)):
            s.append(sl[fml] + srtonos[fml])
        #s = sl + sr[::-1]
        jmax = []
        for e in range(len(s)):
            if s[e] == max(s):
                jmax.append(e)
        print(jmax)
        for j in jmax:
            wwl, zzl = hirschberg(A[:i], B[:j])
            wwr, zzr = hirschberg(A[i:], B[j:])
            #DE TSEKARW TH MONADIKOTHTA
            ww =  wwl + wwr
            zz = zzl + zzr
    return ww, zz
        
print(hirschberg(sys.argv[7], sys.argv[8]))
#el, eos = hirschberg(sys.argv[7], sys.argv[8])
