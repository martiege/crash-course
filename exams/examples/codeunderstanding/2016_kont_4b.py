
def f(b): 
    c=len(b[0])
    d=len(b)
    g = [[0 for row in range(d)]
        for col in range(c)]
    for e in range(0, c):
        for f in range(0, d): 
            g[e][f] = b[f][e]
    return g

mat = [[3, 5], [2, 4], [1, 3]]
print(mat)
print(f(mat))
