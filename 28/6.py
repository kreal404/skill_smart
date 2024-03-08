def PatternUnlock (N, hits):
    a = [[0,1], [0,0], [0,-1], [-1,-1], [-1,0], [-1,1], [1,-1], [1,0], [1,1]]
    counter = 0
    for i in range(1, N):
        b = a[hits[i-1]-1]
        c = a[hits[i]-1]
        counter += ((c[1]-b[1])**2 + (b[0]-c[0])**2)**0.5
    cn = round(counter, 5)
    s = str(cn)
    s = s.replace('0','')
    s = s.replace('.','')
    return s


