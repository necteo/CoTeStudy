# qsort.py

def qsort(v, s, e):
    pivot = v[s]
    bs = s
    be = e
    while s < e:
        while pivot <= v[e] and s < e:
            e -= 1
        if s > e:
            break
        while pivot >= v[s] and s < e:
            s += 1
        if s > e:
            break
        v[s], v[e] = v[e], v[s]
        
    v[bs], v[s] = v[s], v[bs]
    if bs < s:
        qsort(v, bs, s - 1)
    if be > e:
        qsort(v, s + 1, be)
