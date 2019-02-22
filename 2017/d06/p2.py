#!/usr/bin/python3

with open('d6.in') as f:
    buf = list(map(lambda x: int(x), f.readline().strip().split()))
    l = len(buf)
    s = 0
    
    hashes = []
    while True:
        s += 1

        mxv = max(buf)
        mxp = buf.index(mxv)
        buf[mxp] = 0

        i = mxp + 1
        while mxv > 0:
            if i == l:
                i = 0
            buf[i] += 1
            mxv -= 1
            i += 1
        
        print('step {}'.format(s))
        print(buf)

        h = ','.join(map(lambda x: str(x), buf))
        if h in hashes:
            print(s - hashes.index(h) - 1)
            break
        else:
            hashes.append(h)

