import math
import sys
import hashlib

with open(sys.argv[1], 'r') as f:
    n = -1
    nums = []
    while True:
        n = n + 1
        contents = f.readline()
        if len(contents) == 0 :
            break
        nums.append(int(contents))
    m = max(nums)
  
    if (round(math.log(int(m)/n, 2)) - math.log(int(m)/n, 2) > 0 ):
        l = round(math.log(int(m)/n, 2)) - 1
    else:
        l = round(math.log(int(m)/n, 2)) 

    bt = list(nums)
    ltemp = bytearray()
    lcap = bytearray()
    lfin = bytearray()
    utemp = bytearray()
    ucap = bytearray()
    ufin = bytearray()

    #Construct L
    lindex = -1
    for i in range (len(bt)):
        mask = ( 1 << l) - 1
        lastbits = bt[i] & mask
        ltemp.append(lastbits)
        mask = 1
        for x in range(l):
            lastbit = ltemp[i] & mask
            lcap.append(lastbit)
            ltemp[i] = ltemp[i] >> 1
            lindex = lindex + 1
        w = 0
        invert = l
        while ( w < invert):
            temp = lcap[lindex + w - (l - 1)]
            lcap[lindex + w - (l - 1)] = lcap[lindex - w]
            lcap[lindex - w] = temp
            w = w + 1
            invert = invert - 1
    #check an einai full ta bytes
    full = len(lcap) % 8
    if (full != 0) :
        for i in range (8 - full):
            lcap.append(0)
    #Bit creation
    i = 0
    while i < len(lcap):
        s = 1
        temp = lcap[i] << 7
        if i != len(lcap):
            while (s < 8):
                temp = temp | ((lcap[i+s] << 7) >> s)
                s = s + 1
        lfin.append(temp)
        i = i + 8

    #Construct U
    for i in range (len(bt)):
        if i == 0:
            utemp.append(bt[i] >> l)
        #to b-a thing
        else:
            utemp.append((bt[i] >> l) - (bt[i-1] >> l))

    for i in range(len(utemp)):
        x = 0
        while (x <= utemp[i]):
            if ( x == utemp[i]):
                ucap.append(1)
            else:
                ucap.append(0)
            x = x + 1
    #check an einai full ta bytes
    full = len(ucap) % 8
    if (full != 0) :
        for i in range (8 - full):
            ucap.append(0)
    #Bit creation
    i = 0
    while i < len(ucap):
        s = 1
        temp = ucap[i] << 7
        if i != len(ucap):
            while (s < 8):
                temp = temp | ((ucap[i+s] << 7) >> s)
                s = s + 1
        ufin.append(temp)
        i = i + 8

    #print 'em
    m = hashlib.sha256()
    m.update(lfin)
    m.update(ufin)
    digest = m.hexdigest()
    print("l " +str(l))
    print("L")
    for i in range(len(lfin)):
        print(format(lfin[i], "08b"))
    print("U")
    for i in range(len(ufin)):
        print(format(ufin[i], "08b"))
    print(digest)
